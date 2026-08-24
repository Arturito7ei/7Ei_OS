#!/usr/bin/env python3
"""
Generate a self-contained HTML dashboard from github-rising-radar snapshots.

Reads data/latest.json and the prior snapshot for delta climbers.
Output: skills/github-rising-radar/dashboard/index.html (or --output path)

Usage:
    python3 scripts/generate_dashboard.py
    python3 scripts/generate_dashboard.py --output ~/.buzz/RESEARCH/GITHUB_RADAR_DASHBOARD.html
"""

from __future__ import annotations

import argparse
import html
import json
from datetime import datetime, timezone
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_ROOT / "data"
LATEST_PATH = DATA_DIR / "latest.json"
SNAPSHOT_DIR = DATA_DIR / "snapshots"
DEFAULT_OUTPUT = SKILL_ROOT / "dashboard" / "index.html"

TRACK_LABELS = {
    "ai": "AI / LLM",
    "agent": "Agent / MCP",
    "skills": "Agent Skills",
    "devtools": "Dev Tools",
    "general": "General Rising",
}

LANG_COLORS = {
    "TypeScript": "#3178c6",
    "JavaScript": "#f7df1e",
    "Python": "#3572a5",
    "Rust": "#dea584",
    "Go": "#00add8",
    "C": "#555555",
    "Java": "#b07219",
    "HTML": "#e34c26",
}


def load_latest() -> dict:
    if not LATEST_PATH.exists():
        raise SystemExit(f"No {LATEST_PATH} — run scan.py first.")
    return json.loads(LATEST_PATH.read_text())


def load_previous_snapshot(current_scanned_at: str) -> dict[str, dict]:
    if not SNAPSHOT_DIR.exists():
        return {}
    snaps = sorted(SNAPSHOT_DIR.glob("*.json"))
    prev_repos: dict[str, dict] = {}
    for snap in snaps:
        data = json.loads(snap.read_text())
        if data.get("scanned_at") == current_scanned_at:
            continue
        for r in data.get("repos", []):
            prev_repos[r["full_name"]] = r
        break  # most recent prior snapshot only
    return prev_repos


def fmt_num(n: int | float) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 10_000:
        return f"{n / 1_000:.1f}k"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(int(n) if isinstance(n, float) and n == int(n) else round(n, 1))


def build_climbers(repos: list[dict], previous: dict[str, dict]) -> list[dict]:
    climbers = []
    for r in repos:
        prev = previous.get(r["full_name"])
        if not prev:
            continue
        delta = r["stargazers_count"] - prev["stargazers_count"]
        if delta > 0:
            climbers.append({**r, "star_delta": delta})
    climbers.sort(key=lambda x: x["star_delta"], reverse=True)
    return climbers


def render_html(data: dict, previous: dict[str, dict]) -> str:
    repos = data.get("repos", [])
    scanned_at = data.get("scanned_at", "")
    tracks = data.get("tracks", [])
    climbers = build_climbers(repos, previous)
    top_velocity = sorted(repos, key=lambda x: x.get("stars_per_day", 0), reverse=True)[:12]

    try:
        scan_dt = datetime.strptime(scanned_at, "%Y-%m-%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        scan_label = scan_dt.strftime("%Y-%m-%d %H:%M UTC")
    except ValueError:
        scan_label = scanned_at or "unknown"

    total_repos = len(repos)
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    top_climber = climbers[0] if climbers else None
    top_vel = top_velocity[0] if top_velocity else None

    # Group by track
    by_track: dict[str, list] = {}
    for r in repos:
        by_track.setdefault(r.get("_track", "general"), []).append(r)
    for tid in by_track:
        by_track[tid].sort(key=lambda x: x.get("stars_per_day", 0), reverse=True)

    def esc(s: str) -> str:
        return html.escape(s or "")

    def repo_card(r: dict, show_delta: bool = False) -> str:
        lang = r.get("language") or "—"
        color = LANG_COLORS.get(lang, "#6b7280")
        delta_html = ""
        if show_delta and r.get("star_delta"):
            delta_html = f'<span class="delta">+{fmt_num(r["star_delta"])}</span>'
        desc = esc((r.get("description") or "")[:120])
        topics = r.get("topics") or []
        topic_html = "".join(f'<span class="topic">{esc(t)}</span>' for t in topics[:4])
        return f"""
        <article class="repo-card" data-track="{esc(r.get('_track', 'general'))}">
          <header>
            <a class="repo-name" href="{esc(r['html_url'])}" target="_blank" rel="noopener">{esc(r['full_name'])}</a>
            {delta_html}
          </header>
          <p class="desc">{desc}</p>
          <div class="metrics">
            <span class="metric"><strong>{fmt_num(r.get('stars_per_day', 0))}</strong> ⭐/day</span>
            <span class="metric"><strong>{fmt_num(r.get('stargazers_count', 0))}</strong> total</span>
            <span class="metric"><strong>{r.get('age_days', '—')}</strong>d old</span>
            <span class="lang" style="--lang-color:{color}">{esc(lang)}</span>
          </div>
          <div class="topics">{topic_html}</div>
        </article>"""

    climber_cards = "".join(repo_card(r, show_delta=True) for r in climbers[:15])
    velocity_cards = "".join(repo_card(r) for r in top_velocity)

    track_tabs = "".join(
        f'<button class="tab{" active" if i == 0 else ""}" data-track="{esc(tid)}">{esc(TRACK_LABELS.get(tid, tid))} ({len(by_track.get(tid, []))})</button>'
        for i, tid in enumerate(tracks)
    )

    track_sections = ""
    for tid in tracks:
        track_repos = by_track.get(tid, [])[:12]
        cards = "".join(repo_card(r) for r in track_repos)
        track_sections += f"""
        <section class="track-panel" data-track="{esc(tid)}" hidden>
          <h2>{esc(TRACK_LABELS.get(tid, tid))}</h2>
          <div class="card-grid">{cards or '<p class="empty">No repos in this track.</p>'}</div>
        </section>"""

    max_delta = climbers[0]["star_delta"] if climbers else 1
    bar_rows = ""
    for r in climbers[:10]:
        pct = min(100, round(100 * r["star_delta"] / max_delta))
        bar_rows += f"""
        <div class="bar-row">
          <a class="bar-label" href="{esc(r['html_url'])}" target="_blank">{esc(r['full_name'].split('/')[-1])}</a>
          <div class="bar-track"><div class="bar-fill" style="width:{pct}%"></div></div>
          <span class="bar-val">+{fmt_num(r['star_delta'])}</span>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>7Ei GitHub Rising Radar</title>
<style>
:root {{
  --bg: #0d1117;
  --surface: #161b22;
  --border: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  --fire: #f78166;
  --green: #3fb950;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.5; min-height: 100vh; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
header.page {{ padding: 2rem 2rem 1rem; border-bottom: 1px solid var(--border); }}
header.page h1 {{ font-size: 1.75rem; font-weight: 600; letter-spacing: -0.02em; }}
header.page .sub {{ color: var(--muted); font-size: 0.9rem; margin-top: 0.25rem; }}
.badge {{ display: inline-block; background: #21262d; border: 1px solid var(--border); border-radius: 2em; padding: 0.15rem 0.65rem; font-size: 0.75rem; color: var(--muted); margin-left: 0.5rem; }}
main {{ max-width: 1280px; margin: 0 auto; padding: 1.5rem 2rem 3rem; }}
.kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 2rem; }}
.kpi {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; }}
.kpi .label {{ font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }}
.kpi .value {{ font-size: 1.75rem; font-weight: 700; margin-top: 0.25rem; }}
.kpi .hint {{ font-size: 0.8rem; color: var(--muted); margin-top: 0.25rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
section {{ margin-bottom: 2.5rem; }}
section h2 {{ font-size: 1.15rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }}
section h2 .emoji {{ font-size: 1.25rem; }}
.card-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1rem; }}
.repo-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1rem 1.15rem; transition: border-color 0.15s; }}
.repo-card:hover {{ border-color: var(--accent); }}
.repo-card header {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.4rem; }}
.repo-name {{ font-weight: 600; font-size: 0.95rem; word-break: break-all; }}
.delta {{ background: rgba(247,129,102,0.15); color: var(--fire); font-size: 0.75rem; font-weight: 700; padding: 0.1rem 0.45rem; border-radius: 4px; white-space: nowrap; }}
.desc {{ font-size: 0.82rem; color: var(--muted); margin-bottom: 0.65rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
.metrics {{ display: flex; flex-wrap: wrap; gap: 0.75rem; font-size: 0.78rem; color: var(--muted); margin-bottom: 0.5rem; }}
.metrics strong {{ color: var(--text); }}
.lang {{ font-size: 0.72rem; padding: 0.1rem 0.45rem; border-radius: 4px; background: color-mix(in srgb, var(--lang-color) 20%, transparent); color: var(--lang-color); border: 1px solid color-mix(in srgb, var(--lang-color) 40%, transparent); }}
.topics {{ display: flex; flex-wrap: wrap; gap: 0.35rem; }}
.topic {{ font-size: 0.68rem; background: #21262d; color: var(--muted); padding: 0.1rem 0.4rem; border-radius: 3px; }}
.bar-chart {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; }}
.bar-row {{ display: grid; grid-template-columns: 140px 1fr 70px; gap: 0.75rem; align-items: center; margin-bottom: 0.65rem; }}
.bar-label {{ font-size: 0.82rem; font-weight: 500; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.bar-track {{ height: 8px; background: #21262d; border-radius: 4px; overflow: hidden; }}
.bar-fill {{ height: 100%; background: linear-gradient(90deg, var(--fire), #ffa657); border-radius: 4px; }}
.bar-val {{ font-size: 0.8rem; color: var(--fire); font-weight: 600; text-align: right; }}
.tabs {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }}
.tab {{ background: var(--surface); border: 1px solid var(--border); color: var(--muted); padding: 0.4rem 0.85rem; border-radius: 6px; cursor: pointer; font-size: 0.82rem; }}
.tab:hover {{ color: var(--text); border-color: var(--muted); }}
.tab.active {{ background: #21262d; color: var(--text); border-color: var(--accent); }}
.empty {{ color: var(--muted); font-size: 0.9rem; }}
footer {{ text-align: center; color: var(--muted); font-size: 0.75rem; padding: 2rem; border-top: 1px solid var(--border); }}
@media (max-width: 640px) {{
  header.page, main {{ padding-left: 1rem; padding-right: 1rem; }}
  .bar-row {{ grid-template-columns: 100px 1fr 55px; }}
}}
</style>
</head>
<body>
<header class="page">
  <h1>GitHub Rising Radar <span class="badge">7Ei R&D</span></h1>
  <p class="sub">Star velocity intake · scanned {esc(scan_label)} · tracks: {esc(", ".join(tracks))}</p>
</header>
<main>
  <div class="kpis">
    <div class="kpi">
      <div class="label">Repos tracked</div>
      <div class="value">{total_repos}</div>
      <div class="hint">{len(tracks)} scan tracks</div>
    </div>
    <div class="kpi">
      <div class="label">Combined stars</div>
      <div class="value">{fmt_num(total_stars)}</div>
      <div class="hint">across snapshot</div>
    </div>
    <div class="kpi">
      <div class="label">Top climber Δ</div>
      <div class="value">{("+" + fmt_num(top_climber["star_delta"])) if top_climber else "—"}</div>
      <div class="hint">{esc(top_climber["full_name"].split("/")[-1]) if top_climber else "first scan baseline"}</div>
    </div>
    <div class="kpi">
      <div class="label">Peak velocity</div>
      <div class="value">{fmt_num(top_vel["stars_per_day"]) if top_vel else "—"}</div>
      <div class="hint">{esc(top_vel["full_name"].split("/")[-1]) if top_vel else "—"} ⭐/day</div>
    </div>
  </div>

  <section>
    <h2><span class="emoji">🔥</span> Fastest climbers since last scan</h2>
    <div class="bar-chart">{bar_rows or '<p class="empty">First scan — re-run weekly for delta climbers.</p>'}</div>
  </section>

  <section>
    <h2><span class="emoji">📈</span> Top velocity</h2>
    <div class="card-grid">{velocity_cards or '<p class="empty">No data.</p>'}</div>
  </section>

  <section>
    <h2><span class="emoji">🎯</span> By track</h2>
    <div class="tabs" id="track-tabs">{track_tabs}</div>
    {track_sections}
  </section>

  <section>
    <h2><span class="emoji">🔥</span> All climbers (detail)</h2>
    <div class="card-grid">{climber_cards or '<p class="empty">No deltas vs previous snapshot.</p>'}</div>
  </section>
</main>
<footer>
  Generated by <code>github-rising-radar/scripts/generate_dashboard.py</code> ·
  BYOK via <code>gh</code> CLI · Next: <code>tech-radar-evaluate</code> → <code>RD_CANDIDATE_QUEUE.md</code>
</footer>
<script>
document.querySelectorAll('#track-tabs .tab').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('#track-tabs .tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.track-panel').forEach(p => p.hidden = true);
    btn.classList.add('active');
    const panel = document.querySelector('.track-panel[data-track="' + btn.dataset.track + '"]');
    if (panel) panel.hidden = false;
  }});
}});
const firstPanel = document.querySelector('.track-panel');
if (firstPanel) firstPanel.hidden = false;
</script>
</body>
</html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GitHub Rising Radar HTML dashboard")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    data = load_latest()
    previous = load_previous_snapshot(data.get("scanned_at", ""))
    html_out = render_html(data, previous)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_out)
    print(f"Dashboard: {args.output}")


if __name__ == "__main__":
    main()
