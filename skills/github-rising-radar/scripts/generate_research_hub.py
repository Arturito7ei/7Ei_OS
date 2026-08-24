#!/usr/bin/env python3
"""
Generate the 7Ei weekly research hub for GitHub Pages (docs/).

Reads radar scan + chooser markdown from the Buzz nest RESEARCH/ dir,
copies the radar HTML dashboard, and writes docs/index.html + docs/reports/*.html.

Usage:
    python3 skills/github-rising-radar/scripts/generate_research_hub.py
    python3 skills/github-rising-radar/scripts/generate_research_hub.py \\
        --research-dir ~/.buzz/RESEARCH --output-dir docs
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = SKILL_ROOT.parent.parent
DEFAULT_RESEARCH = Path.home() / ".buzz" / "RESEARCH"
DEFAULT_OUTPUT = REPO_ROOT / "docs"
DASHBOARD_SRC = SKILL_ROOT / "dashboard" / "index.html"

PAGE_CSS = """
:root {
  --bg: #0d1117; --surface: #161b22; --border: #30363d;
  --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff;
  --green: #3fb950; --fire: #f78166;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.55; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.layout { display: grid; grid-template-columns: 240px 1fr; min-height: 100vh; }
nav { background: var(--surface); border-right: 1px solid var(--border); padding: 1.5rem 1rem; }
nav h1 { font-size: 1rem; font-weight: 600; margin-bottom: 0.25rem; }
nav .sub { font-size: 0.75rem; color: var(--muted); margin-bottom: 1.25rem; }
nav ul { list-style: none; }
nav li { margin-bottom: 0.35rem; }
nav a { font-size: 0.85rem; color: var(--muted); display: block; padding: 0.35rem 0.5rem; border-radius: 6px; }
nav a:hover, nav a.active { background: #21262d; color: var(--text); text-decoration: none; }
main { padding: 2rem 2.5rem 4rem; max-width: 960px; }
.hero { margin-bottom: 2rem; }
.hero h2 { font-size: 1.6rem; font-weight: 600; letter-spacing: -0.02em; }
.hero p { color: var(--muted); margin-top: 0.5rem; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin: 1.5rem 0 2.5rem; }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; }
.card h3 { font-size: 0.95rem; margin-bottom: 0.35rem; }
.card p { font-size: 0.82rem; color: var(--muted); }
.card .cta { display: inline-block; margin-top: 0.75rem; font-size: 0.82rem; font-weight: 600; }
.badge { display: inline-block; background: rgba(63,185,80,0.15); color: var(--green); font-size: 0.7rem; font-weight: 600; padding: 0.15rem 0.5rem; border-radius: 999px; margin-left: 0.35rem; }
section { margin-bottom: 2rem; }
section h3 { font-size: 1.05rem; margin-bottom: 0.75rem; }
.week-list { display: flex; flex-direction: column; gap: 0.5rem; }
.week-row { display: flex; justify-content: space-between; align-items: center; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; padding: 0.65rem 1rem; font-size: 0.88rem; }
.week-row .date { color: var(--muted); font-size: 0.78rem; }
.report-body h1 { font-size: 1.5rem; margin-bottom: 1rem; }
.report-body h2 { font-size: 1.15rem; margin: 1.5rem 0 0.75rem; }
.report-body h3 { font-size: 1rem; margin: 1.25rem 0 0.5rem; }
.report-body p { margin: 0.75rem 0; color: var(--muted); }
.report-body table { width: 100%; border-collapse: collapse; font-size: 0.82rem; margin: 1rem 0; }
.report-body th, .report-body td { border: 1px solid var(--border); padding: 0.45rem 0.6rem; text-align: left; }
.report-body th { background: var(--surface); color: var(--muted); font-weight: 600; }
.report-body tr:nth-child(even) td { background: rgba(22,27,34,0.5); }
.report-body code { background: #21262d; padding: 0.1rem 0.35rem; border-radius: 4px; font-size: 0.85em; }
.report-body hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
.report-body em { color: var(--muted); font-size: 0.85rem; }
footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border); font-size: 0.78rem; color: var(--muted); }
@media (max-width: 768px) { .layout { grid-template-columns: 1fr; } nav { border-right: none; border-bottom: 1px solid var(--border); } }
"""


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3 :].lstrip()
    return text


def md_inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(text: str) -> str:
    text = strip_frontmatter(text)
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            out.append(f"<h1>{md_inline(line[2:])}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{md_inline(line[3:])}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{md_inline(line[4:])}</h3>")
        elif line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1]):
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[\s\-:|]+\|$", lines[i]):
                    cells = [c.strip() for c in lines[i].strip("|").split("|")]
                    rows.append(cells)
                i += 1
            i -= 1
            if rows:
                out.append("<table><thead><tr>" + "".join(f"<th>{md_inline(c)}</th>" for c in rows[0]) + "</tr></thead><tbody>")
                for row in rows[1:]:
                    out.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in row) + "</tr>")
                out.append("</tbody></table>")
        elif line.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].startswith("- "):
                out.append(f"<li>{md_inline(lines[i][2:])}</li>")
                i += 1
            out.append("</ul>")
            i -= 1
        elif line.strip() == "---":
            out.append("<hr>")
        elif line.startswith("*") and line.endswith("*"):
            out.append(f"<p><em>{md_inline(line.strip('*'))}</em></p>")
        elif line.strip():
            out.append(f"<p>{md_inline(line)}</p>")
        i += 1
    return "\n".join(out)


def discover_weeks(research_dir: Path) -> list[str]:
    dates: set[str] = set()
    for pat in ("GITHUB_RISING_RADAR_*.md", "WEEKLY_SKILL_CHOOSER_*.md"):
        for p in research_dir.glob(pat):
            m = re.search(r"(\d{4}_\d{2}_\d{2})", p.name)
            if m:
                dates.add(m.group(1).replace("_", "-"))
    return sorted(dates, reverse=True)


def week_slug(date: str) -> str:
    return date  # already YYYY-MM-DD


def load_week_content(research_dir: Path, date: str) -> tuple[str | None, str | None]:
    slug = date.replace("-", "_")
    scan = research_dir / f"GITHUB_RISING_RADAR_{slug}.md"
    chooser = research_dir / f"WEEKLY_SKILL_CHOOSER_{slug}.md"
    scan_text = scan.read_text() if scan.exists() else None
    chooser_text = chooser.read_text() if chooser.exists() else None
    return scan_text, chooser_text


def page_shell(title: str, nav_active: str, body: str, weeks: list[str]) -> str:
    nav_links = ['<li><a href="index.html"' + (' class="active"' if nav_active == "home" else "") + ">Home</a></li>"]
    nav_links.append('<li><a href="radar.html"' + (' class="active"' if nav_active == "radar" else "") + ">Radar dashboard</a></li>")
    for w in weeks:
        nav_links.append(
            f'<li><a href="reports/{week_slug(w)}.html"'
            + (' class="active"' if nav_active == w else "")
            + f">{w}</a></li>"
        )
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — 7Ei Research</title>
<style>{PAGE_CSS}</style>
</head>
<body>
<div class="layout">
<nav>
  <h1>7Ei Research</h1>
  <p class="sub">Weekly radar · chooser · evals</p>
  <ul>{"".join(nav_links)}</ul>
</nav>
<main>{body}
<footer>Generated {generated} · <code>generate_research_hub.py</code> · Owner: 7RD</footer>
</main>
</div>
</body>
</html>"""


def render_index(weeks: list[str], latest: str | None) -> str:
    latest_card = ""
    if latest:
        latest_card = f"""
<div class="card">
  <h3>Latest week <span class="badge">current</span></h3>
  <p>Scan + skill chooser for {latest}</p>
  <a class="cta" href="reports/{week_slug(latest)}.html">Open report →</a>
</div>"""
    week_rows = "".join(
        f'<div class="week-row"><a href="reports/{week_slug(w)}.html">Week of {w}</a><span class="date">scan + chooser</span></div>'
        for w in weeks
    )
    body = f"""
<div class="hero">
  <h2>Weekly Research Hub</h2>
  <p>GitHub Rising Radar scans, skill chooser slates, and interactive dashboard — published from the Buzz nest after each Monday scan.</p>
</div>
<div class="cards">
  <div class="card">
    <h3>Radar dashboard</h3>
    <p>Interactive climbers, track tabs, KPI cards — star velocity from <code>gh</code> BYOK scans.</p>
    <a class="cta" href="radar.html">Open dashboard →</a>
  </div>
  {latest_card}
  <div class="card">
    <h3>Skill catalog</h3>
    <p>Source of truth for agent skills — bind by path, never bulk-load.</p>
    <a class="cta" href="https://github.com/Arturito7ei/7Ei_OS/blob/main/skills/catalog.md">catalog.md →</a>
  </div>
</div>
<section>
  <h3>Archive</h3>
  <div class="week-list">{week_rows or '<p class="sub">No weekly reports found.</p>'}</div>
</section>"""
    return page_shell("Weekly Research Hub", "home", body, weeks)


def render_week_report(date: str, scan: str | None, chooser: str | None, weeks: list[str]) -> str:
    parts = [f'<div class="hero"><h2>Week of {date}</h2><p><a href="radar.html">Open interactive radar dashboard →</a></p></div>']
    parts.append('<div class="report-body">')
    if chooser:
        parts.append(md_to_html(chooser))
        parts.append("<hr>")
    if scan:
        parts.append(md_to_html(scan))
    elif not chooser:
        parts.append("<p>No scan or chooser files found for this week.</p>")
    parts.append("</div>")
    return page_shell(f"Week of {date}", date, "\n".join(parts), weeks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate 7Ei research hub for GitHub Pages")
    parser.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    research_dir: Path = args.research_dir.expanduser()
    output_dir: Path = args.output_dir
    reports_dir = output_dir / "reports"

    if not research_dir.is_dir():
        raise SystemExit(f"Research dir not found: {research_dir}")

    weeks = discover_weeks(research_dir)
    latest = weeks[0] if weeks else None

    output_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Refresh radar dashboard from latest.json if present
    if (SKILL_ROOT / "data" / "latest.json").exists():
        import subprocess
        subprocess.run(
            ["python3", str(Path(__file__).with_name("generate_dashboard.py")), "--output", str(DASHBOARD_SRC)],
            check=True,
        )

    if DASHBOARD_SRC.exists():
        shutil.copy2(DASHBOARD_SRC, output_dir / "radar.html")
    else:
        raise SystemExit(f"Missing dashboard: {DASHBOARD_SRC}")

    (output_dir / "index.html").write_text(render_index(weeks, latest))

    for w in weeks:
        scan, chooser = load_week_content(research_dir, w)
        if scan or chooser:
            (reports_dir / f"{week_slug(w)}.html").write_text(render_week_report(w, scan, chooser, weeks))

    print(f"Hub: {output_dir / 'index.html'}")
    print(f"Dashboard: {output_dir / 'radar.html'}")
    print(f"Weeks: {len(weeks)}")


if __name__ == "__main__":
    main()
