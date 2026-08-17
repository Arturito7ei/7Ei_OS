#!/usr/bin/env python3
"""
Scan GitHub for fast-rising repositories via gh CLI (BYOK).

Computes star velocity (stars/day) and delta since last snapshot.
Requires: gh auth login (or GH_TOKEN).

Usage:
    python3 scripts/scan.py [--tracks ai,agent,mcp,general] [--days 90] [--min-stars 50]
    python3 scripts/scan.py --report-only
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_ROOT / "data"
SNAPSHOT_DIR = DATA_DIR / "snapshots"
LATEST_PATH = DATA_DIR / "latest.json"

# Tracks tuned for 7Ei R&D intake — edit queries here
DEFAULT_TRACKS = {
    "ai": {
        "label": "AI / LLM",
        "query": "topic:llm",
    },
    "agent": {
        "label": "Agent / MCP",
        "query": "topic:mcp-server",
    },
    "skills": {
        "label": "Agent Skills",
        "query": "agentskills in:name,description,readme",
    },
    "devtools": {
        "label": "Dev Tools",
        "query": "topic:developer-tools",
    },
    "general": {
        "label": "General Rising",
        "query": "",
    },
}


def run_gh_search(query: str, days: int, min_stars: int, per_page: int = 30) -> list[dict]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    parts = [f"stars:>{min_stars}", f"created:>{cutoff}"]
    if query.strip():
        parts.insert(0, f"({query})")
    q = " ".join(parts)

    cmd = [
        "gh",
        "api",
        f"/search/repositories?q={quote(q)}&sort=stars&order=desc&per_page={per_page}",
        "--jq",
        ".items[] | {full_name, html_url, description, stargazers_count, created_at, pushed_at, language, topics, license: .license.spdx_id}",
    ]
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"gh search failed: {e.stderr}", file=sys.stderr)
        sys.exit(1)

    repos = []
    for line in out.strip().splitlines():
        if not line.strip():
            continue
        repos.append(json.loads(line))
    return repos


def age_days(created_at: str) -> float:
    created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - created
    return max(delta.total_seconds() / 86400, 1.0)


def enrich(repo: dict) -> dict:
    stars = repo.get("stargazers_count") or 0
    days = age_days(repo["created_at"])
    velocity = round(stars / days, 1)
    return {
        **repo,
        "age_days": round(days, 1),
        "stars_per_day": velocity,
    }


def load_previous() -> dict[str, dict]:
    if not LATEST_PATH.exists():
        return {}
    data = json.loads(LATEST_PATH.read_text())
    return {r["full_name"]: r for r in data.get("repos", [])}


def save_snapshot(all_repos: list[dict], tracks_scanned: list[str]) -> Path:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    payload = {
        "scanned_at": ts,
        "tracks": tracks_scanned,
        "repos": all_repos,
    }
    snap_path = SNAPSHOT_DIR / f"{ts}.json"
    snap_path.write_text(json.dumps(payload, indent=2))
    LATEST_PATH.write_text(json.dumps(payload, indent=2))
    return snap_path


def render_report(all_repos: list[dict], previous: dict[str, dict], tracks: dict) -> str:
    lines = [
        f"# GitHub Rising Radar — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "Star velocity = total stars ÷ repo age (days). Delta = stars since last scan.",
        "",
    ]

    # Top climbers since last scan
    climbers = []
    for r in all_repos:
        prev = previous.get(r["full_name"])
        delta = r["stargazers_count"] - (prev["stargazers_count"] if prev else 0)
        if delta > 0 and prev:
            climbers.append({**r, "star_delta": delta})
    climbers.sort(key=lambda x: x["star_delta"], reverse=True)

    if climbers:
        lines += ["## 🔥 Fastest climbers since last scan", ""]
        lines += ["| Repo | Δ stars | ⭐/day | Total | Age (d) |", "|---|---:|---:|---:|---:|"]
        for r in climbers[:15]:
            lines.append(
                f"| [{r['full_name']}]({r['html_url']}) | +{r['star_delta']} | {r['stars_per_day']} | {r['stargazers_count']} | {r['age_days']} |"
            )
        lines.append("")
    elif previous:
        lines += ["*No star deltas vs previous snapshot (same scan window).*", ""]
    else:
        lines += ["*First scan — no delta baseline yet. Re-run weekly for 🔥 climbers.*", ""]

    # By track — top velocity
    by_track: dict[str, list] = {}
    for r in all_repos:
        by_track.setdefault(r.get("_track", "general"), []).append(r)

    for track_id, track_repos in by_track.items():
        label = tracks.get(track_id, {}).get("label", track_id)
        ranked = sorted(track_repos, key=lambda x: x["stars_per_day"], reverse=True)[:10]
        lines += [f"## {label} — top velocity", ""]
        lines += ["| Repo | ⭐/day | Total | Language |", "|---|---:|---:|---|"]
        for r in ranked:
            desc = (r.get("description") or "")[:60].replace("|", "/")
            lines.append(
                f"| [{r['full_name']}]({r['html_url']}) | {r['stars_per_day']} | {r['stargazers_count']} | {r.get('language') or '—'} |"
            )
        lines.append("")

    lines += [
        "---",
        "*Next: run `tech-radar-evaluate` on interesting candidates → append `RESEARCH/RD_CANDIDATE_QUEUE.md`*",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan rising GitHub repos")
    parser.add_argument("--tracks", default="ai,agent,devtools,general", help="Comma-separated track ids")
    parser.add_argument("--days", type=int, default=90, help="Lookback window for created: filter")
    parser.add_argument("--min-stars", type=int, default=50, help="Minimum star count")
    parser.add_argument("--per-page", type=int, default=25, help="Results per track")
    parser.add_argument("--report-only", action="store_true", help="Render from latest.json only")
    parser.add_argument("--output", type=Path, help="Write markdown report to file")
    args = parser.parse_args()

    track_ids = [t.strip() for t in args.tracks.split(",") if t.strip()]
    previous = load_previous()

    if args.report_only:
        if not LATEST_PATH.exists():
            print("No latest.json — run a scan first.", file=sys.stderr)
            sys.exit(1)
        data = json.loads(LATEST_PATH.read_text())
        report = render_report(data["repos"], previous, DEFAULT_TRACKS)
        print(report)
        return

    seen: set[str] = set()
    all_repos: list[dict] = []

    for tid in track_ids:
        if tid not in DEFAULT_TRACKS:
            print(f"Unknown track: {tid}", file=sys.stderr)
            continue
        track = DEFAULT_TRACKS[tid]
        repos = run_gh_search(track["query"], args.days, args.min_stars, args.per_page)
        for repo in repos:
            name = repo["full_name"]
            if name in seen:
                continue
            seen.add(name)
            enriched = enrich(repo)
            enriched["_track"] = tid
            all_repos.append(enriched)

    all_repos.sort(key=lambda x: x["stars_per_day"], reverse=True)
    snap = save_snapshot(all_repos, track_ids)
    report = render_report(all_repos, previous, DEFAULT_TRACKS)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
        print(f"Report: {args.output}", file=sys.stderr)
    else:
        print(report)

    print(f"Snapshot: {snap}", file=sys.stderr)


if __name__ == "__main__":
    main()
