# Skill Catalog

> **⚠️ CANONICAL SOURCE** — This file is the single source of truth for all 7Ei agent skills.
>
> **For agents:** Always read this file first. It lists every available skill, what it does, and where its `SKILL.md` lives.
>
> **To add/edit a skill:** Edit `skills/<name>/SKILL.md`, update this catalog, then run `python3 skills/sync_vault.py` to regenerate the Obsidian vault.
>
> **Last updated:** 2026-08-19

---

## Skill File Locations

| Location | Path | Purpose |
|---|---|---|
| **7Ei_OS skills** | `7Ei_OS/skills/<name>/SKILL.md` | Physical skill files — edit here |
| **OpenClaw bundled** | `/opt/homebrew/lib/node_modules/openclaw/skills/<name>/SKILL.md` | Bundled skills — read only |
| **OpenClaw plugin** | `~/.openclaw/plugin-skills/<name>/SKILL.md` | Agent-installed plugins |
| **Workspace skills** | `~/.openclaw/workspace/skills/` | Symlinks to 7Ei_OS skills |

---

## 📊 Finance

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| Kronos | workspace | `skills/kronos/SKILL.md` | K-line foundation model for financial candlestick (OHLCV) forecasting. AAAI 2026. HuggingFace: `NeoQuasar/Kronos-*`. |
| OpenBB MCP | workspace | — | 219 financial data tools via MCP (equity, crypto, macro, fixed income, SEC filings, futures, options, news). Running on Mac mini (`http://192.168.1.228:8001/mcp`). |

---

## 🎯 Strategy

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| CEO-Review | workspace (gstack) | `skills/gstack-openclaw-ceo-review/SKILL.md` | 4-mode strategic challenge: SCOPE EXPANSION / SELECTIVE / HOLD / REDUCE. |
| Office-Hours | workspace (gstack) | `skills/gstack-openclaw-office-hours/SKILL.md` | 6 forcing questions for product decisions. Startup diagnostic + builder brainstorm modes. |

---

## ⚙️ Engineering

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| Investigate | workspace (gstack) | `skills/gstack-openclaw-investigate/SKILL.md` | Root cause debugging. 4-phase: Investigate → Analyze → Hypothesize → Implement. Iron Law: no fixes without root cause. |
| Retro | workspace (gstack) | `skills/gstack-openclaw-retro/SKILL.md` | Weekly engineering retrospective. Commit history, work patterns, code quality metrics, per-person contributions, trend tracking. |
| Self-Improving-Agent | workspace | `skills/self-improving-agent/SKILL.md` | Capture learnings, errors, corrections across sessions. Promotes after 3 occurrences or 7 days stable. |

---

## 🔄 Operations

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| secret-hygiene | workspace | `skills/secret-hygiene/SKILL.md` | Reference secrets by 1Password item name or scoped env path only. Never paste values into chat, logs, or git. Human-only rotation. |
| n8n-Workflow-Automation | workspace | `skills/n8n-workflow-automation/SKILL.md` | Design robust n8n workflow JSON with idempotency, retry, error handling, human-in-the-loop queues. |

---

## 💻 IT

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| IPTV-Browse | workspace | `skills/iptv-browse/SKILL.md` | Browse/search IPTV channels from iptv-org database. Country + category filters. |
| Browser-Automation | plugin | `~/.openclaw/plugin-skills/browser-automation/SKILL.md` | Control web pages with OpenClaw browser tool. Multi-step flows, login checks, tab management. |
| Healthcheck | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/healthcheck/SKILL.md` | Audit/harden OpenClaw hosts: SSH, firewall, updates, exposure, backups, disk encryption. |
| Obsidian-Markdown | kepano-obsidian | `skills/kepano-obsidian/skills/obsidian-markdown/SKILL.md` | Create/edit Obsidian-flavored Markdown with wikilinks, embeds, callouts, properties. |
| Obsidian-Bases | kepano-obsidian | `skills/kepano-obsidian/skills/obsidian-bases/SKILL.md` | Create/edit Obsidian Bases (.base) with views, filters, formulas, summaries. |
| JSON-Canvas | kepano-obsidian | `skills/kepano-obsidian/skills/json-canvas/SKILL.md` | Create/edit JSON Canvas (.canvas) with nodes, edges, groups, connections. |
| Obsidian-CLI-Skill | kepano-obsidian | `skills/kepano-obsidian/skills/obsidian-cli/SKILL.md` | Interact with Obsidian vaults via CLI including plugin/theme development. |
| Defuddle | kepano-obsidian | `skills/kepano-obsidian/skills/defuddle/SKILL.md` | Extract clean markdown from web pages, removing clutter to save tokens. |

---

## 📢 Communication

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| iMessage | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/imsg/SKILL.md` | Send/receive iMessage/SMS via macOS Messages.app CLI. |
| Apple-Notes | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/apple-notes/SKILL.md` | CRUD on Apple Notes via `memo` CLI on macOS. |
| Apple-Reminders | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/apple-reminders/SKILL.md` | List/add/complete Apple Reminders via `remindctl`. |

---

## 📋 Project Management

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| epic-to-pr | workspace | `skills/epic-to-pr/SKILL.md` | Epic hypothesis → stories → worktree → PR with Buzz channel link. GitHub Issues default; Jira optional per venture. |
| Things-Mac | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/things-mac/SKILL.md` | Manage Things 3 todos, inbox, projects, areas, tags on macOS. |

---

## 🔬 Research

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| tech-radar-evaluate | workspace | `skills/tech-radar-evaluate/SKILL.md` | Evaluate tools/skills for 7Ei: sovereignty-first rubric, adopt/trial/hold/avoid verdict, citations. Use before imports or stack changes. |
| github-rising-radar | workspace | `skills/github-rising-radar/SKILL.md` | Scan rising GitHub repos by star velocity via gh CLI (BYOK). Weekly radar intake; feeds candidate queue; HTML dashboard. |
| gauntlet-loop | workspace | `skills/gauntlet-loop/SKILL.md` | Builder+critic+blind-bar quality loop for creative deliverables (pages, explainers, dashboards). Opt-in only; Cursor Task+loop port. CC BY 4.0. |
| Summarize | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/summarize/SKILL.md` | Summarize/transcribe URLs, YouTube/videos, podcasts, PDFs, articles, local files. |
| Session-Logs | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/session-logs/SKILL.md` | Search and analyze session logs with jq. Find past decisions in older sessions. |

---

## 🌐 Integrations

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| GitHub | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/github/SKILL.md` | Issues, PRs, CI logs, releases, repos via `gh` CLI. Account: Arturito7ei. |
| Notion | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/notion/SKILL.md` | Notion CLI/API for pages, content, data sources, comments, Workers, raw API. |
| 1Password | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/1password/SKILL.md` | Secret injection via 1Password CLI (`op`). Sign-in, desktop integration. |
| X-url | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/xurl/SKILL.md` | Authenticated X posts, replies, DMs, search, media upload via `xurl` CLI. |

---

## 🛠️ Tools

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| Meme-Maker | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/meme-maker/SKILL.md` | Search meme templates and generate image memes. |
| Diagram-Maker | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/diagram-maker/SKILL.md` | Create SVG/HTML or Excalidraw diagrams (concepts, architecture, flows). |
| Video-Frames | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/video-frames/SKILL.md` | Extract frames or short clips from videos via ffmpeg. |
| TTS-Chatterbox | workspace | — | Local voice cloning + TTS via Chatterbox TTS (Python 3.11). Voice clone from reference audio. Reference: `/tmp/thierry_ref.wav`. |
| Nano-PDF | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/nano-pdf/SKILL.md` | Edit PDFs with natural-language instructions via `nano-pdf` CLI. |
| OpenAI-Whisper | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/openai-whisper/SKILL.md` | Local speech-to-text with Whisper CLI. No API key required. |
| Model-Usage | bundled | `/opt/homebrew/lib/node_modules/openclaw/skills/model-usage/SKILL.md` | Summarize Codex/Claude cost logs by model. |

---

## 🚀 7Ei-Specific (Custom)

| Skill | Source | Skill File | Description |
|-------|--------|------------|-------------|
| Kronos Integration | 7Ei_OS | — | OpenBB data → Kronos forecasting pipeline for 7EiBank. |
| Sprint Cycle | 7Ei_OS | — | Plan → execute → merge → deploy → test |
| Memory Management | 7Ei_OS | — | Tiered memory with promotion pipeline |
| Agent Proposal | Mission Control | — | LLM-generated agent profiles |

---

## 📦 skill-library Repo

> Physical reusable skill packages: [Arturito7ei/skill-library](https://github.com/Arturito7ei/skill-library)

| Skill | Domain | Status |
|-------|--------|--------|
| jira-openclaw | Project Management | ✅ Active |

---

## ➕ Adding a New Skill

```
1. Create 7Ei_OS/skills/<name>/SKILL.md          ← physical skill file
2. Add entry to skills/catalog.md                ← register it
3. Run python3 skills/sync_vault.py              ← regenerate Obsidian vault + symlinks
4. git add + commit + PR to 7Ei_OS               ← publish
5. (optional) skill-library/<name>/SKILL.md      ← if reusable across agents
```

**SKILL.md format:** Use `skills/templates/SKILL-TEMPLATE.md` as reference.

**Obsidian vault is auto-generated** from this file by `sync_vault.py`. Do not edit Obsidian notes manually.

---

*Maintained by: Arturito (Arturito7Ei CLAW) — Primary Agent Orchestrator of 7Ei.ai*

---

## External Skill Integrations

### kepano/obsidian-skills

Integrated 2026-06-23 (Option 1A — Fork & Adapt). See `skills/kepano-obsidian/7Ei_OS_ATTRIBUTION.md` for full attribution and upstream sync instructions.

| Skill | Category | Source File | Description |
|-------|----------|-------------|-------------|
| Obsidian-Markdown | IT | `kepano-obsidian/skills/obsidian-markdown/SKILL.md` | Wikilinks, embeds, callouts, properties |
| Obsidian-Bases | IT | `kepano-obsidian/skills/obsidian-bases/SKILL.md` | .base files with views/filters/formulas |
| JSON-Canvas | IT | `kepano-obsidian/skills/json-canvas/SKILL.md` | Canvas nodes, edges, groups |
| Obsidian-CLI-Skill | IT | `kepano-obsidian/skills/obsidian-cli/SKILL.md` | CLI vault interaction |
| Defuddle | Tools | `kepano-obsidian/skills/defuddle/SKILL.md` | Clean web-to-markdown extraction |
*Tool: python3 skills/sync_vault.py*
