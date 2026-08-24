---
name: github-rising-radar
description: Scan GitHub for fast-rising repositories by star velocity using gh CLI (BYOK). Use during weekly radar hour or when asked to watch trending/upcoming repos. Outputs ranked report and feeds RD_CANDIDATE_QUEUE via tech-radar-evaluate.
---

# GitHub Rising Radar

Spot repositories gaining stars *now* — not lifetime leaderboard noise. Local snapshots enable **delta-since-last-scan** (🔥 climbers).

**Cluster:** Research  
**Owner:** 7RD  
**Pairs with:** `tech-radar-evaluate`, `RESEARCH/RD_CANDIDATE_QUEUE.md`  
**Sovereignty:** BYOK via `gh` CLI — no mandatory SaaS. Optional self-hosted trending API (see §Alternatives).

## When to Use

- Weekly radar hour (standing cadence in `RD_SCREENING_STRATEGY_2026_08_13.md`)
- Thierry or 7MAN asks to watch rising / upcoming GitHub repos
- Before cherry-picking external skills from discovered repos
- After major GitHub announcement cycles (new model releases, agent frameworks)

## Prerequisites

```bash
gh auth status   # must be logged in — uses operator's GitHub token
python3 --version  # 3.10+
```

Rate limits: GitHub Search API ≈ 30 req/min authenticated. One scan = one request per track (default 4 tracks).

## Quick Start

From repo root (`7Ei_OS/`):

```bash
# Full scan → markdown report on stdout
python3 skills/github-rising-radar/scripts/scan.py

# Save report to Buzz RESEARCH (recommended for radar hour)
python3 skills/github-rising-radar/scripts/scan.py \
  --output ~/.buzz/RESEARCH/GITHUB_RISING_RADAR_$(date +%Y_%m_%d).md

# Re-render last snapshot without API calls
python3 skills/github-rising-radar/scripts/scan.py --report-only

# HTML dashboard (from latest.json — no API)
python3 skills/github-rising-radar/scripts/generate_dashboard.py
open skills/github-rising-radar/dashboard/index.html
```

## Scan Tracks (default)

| Track | Query focus |
|---|---|
| `ai` | `topic:llm` |
| `agent` | `topic:mcp-server` |
| `skills` | agentskills in name/description |
| `devtools` | `topic:developer-tools` |
| `general` | Broad rising (stars + recency only) |

Customize: `--tracks ai,agent --days 60 --min-stars 100`

## Metrics

| Metric | Formula | Use |
|---|---|---|
| **Star velocity** | `stars ÷ max(age_days, 1)` | Primary rank — early repos gaining fast |
| **Δ stars** | vs previous `data/latest.json` | 🔥 climbers since last weekly scan |
| **Age (days)** | from `created_at` | Prefer &lt;90d for "upcoming" |

**Do not** treat total stars alone as signal — old famous repos coast.

## Workflow (radar hour)

1. **Scan** — run `scan.py`, save report to `~/.buzz/RESEARCH/GITHUB_RISING_RADAR_YYYY_MM_DD.md`
2. **Triage** — pick 3–10 interesting repos (problem fit for 7Ei clusters)
3. **Score** — run `tech-radar-evaluate` on each; append rows to `RD_CANDIDATE_QUEUE.md`
4. **Announce** — post top 🔥 climbers in `#research`; escalate Adopt/Trial to 7MAN

## Output Artifacts

| Path | Purpose |
|---|---|
| `skills/github-rising-radar/data/latest.json` | Last scan (for deltas) |
| `skills/github-rising-radar/data/snapshots/*.json` | Historical snapshots |
| `~/.buzz/RESEARCH/GITHUB_RISING_RADAR_*.md` | Human-readable weekly report |
| `skills/github-rising-radar/dashboard/index.html` | Self-contained HTML dashboard (regenerate via `generate_dashboard.py`) |

Snapshot data is gitignored — lives on operator machine only.

## Dashboard

After each scan, regenerate the dashboard:

```bash
python3 skills/github-rising-radar/scripts/generate_dashboard.py
```

Quality bar (gauntlet-loop trial): GitHub Trending at-a-glance cards + ThoughtWorks Radar track clarity. For polished visual passes on the dashboard itself, bind `gauntlet-loop` skill.

## Limitations

- **No official GitHub Trending API** — we reconstruct via Search API + velocity (GitHub docs: no trending endpoint). Verified 2026-08-13.
- Search index lag ~ minutes; not real-time tick data.
- Spam / star-bought repos appear — triage with `pushed_at`, commit activity, README quality.
- Tracks are keyword/topic heuristics — edit `DEFAULT_TRACKS` in `scripts/scan.py` for new clusters.

## Alternatives (evaluated 2026-08-13)

| Option | Sovereignty | Verdict |
|---|---|---|
| **`gh search` + this skill** | BYOK, local snapshots | **Adopt** — default path |
| [NiklasTiede/Github-Trending-API](https://github.com/NiklasTiede/Github-Trending-API) MIT, Docker, scrape trending HTML | Self-hostable | **Trial** if we need exact trending-page parity |
| [korbinjoe/trending8](https://github.com/korbinjoe/trending8) | Self-hostable Postgres | **Hold** — heavier ops; revisit if scan.py insufficient |
| Public trending mirrors (ghapi.huchen.dev, etc.) | Third-party SaaS | **Avoid** for default — Precedence 01 |

## Quality Checklist

- [ ] `gh auth status` OK before scan
- [ ] Report saved to RESEARCH with date stamp
- [ ] Top 3–10 candidates queued or scored
- [ ] Verified vs read distinguished in queue citations
- [ ] No fleet install from discovery — score first

## Example

```bash
$ python3 skills/github-rising-radar/scripts/scan.py --tracks ai,agent --min-stars 100
# GitHub Rising Radar — 2026-08-13 12:00 UTC
## 🔥 Fastest climbers since last scan
| Repo | Δ stars | ⭐/day | ...
```

First run shows velocity only; second weekly run surfaces 🔥 deltas.
