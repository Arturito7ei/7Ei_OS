# Skill Catalog

> Master list of all available skills across the 7Ei ecosystem.
> **Last updated:** 2026-06-22
>
> **Canonical sources:**
> - OpenClaw workspace: `~/.openclaw/workspace/skills/`
> - OpenClaw bundled: `/opt/homebrew/lib/node_modules/openclaw/skills/`
> - OpenClaw plugins: `~/.openclaw/plugin-skills/`
> - Obsidian working index: `TARCO-MC_Vault/Skill-Library/`

---

## 📊 Finance

| Skill | Source | Description |
|-------|--------|------------|
| Kronos | workspace | K-line foundation model for financial candlestick (OHLCV) forecasting. AAAI 2026. HuggingFace: `NeoQuasar/Kronos-*`. |
| OpenBB MCP | workspace | 219 financial data tools via MCP (equity, crypto, macro, fixed income, SEC filings, futures, options, news). Running on Mac mini. |

---

## 🎯 Strategy

| Skill | Source | Description |
|-------|--------|------------|
| CEO-Review | workspace (gstack) | 4-mode strategic challenge: SCOPE EXPANSION / SELECTIVE / HOLD / REDUCE. Poke holes in plans. |
| Office-Hours | workspace (gstack) | 6 forcing questions for product decisions. Startup diagnostic + builder brainstorm modes. |

---

## ⚙️ Engineering

| Skill | Source | Description |
|-------|--------|------------|
| Investigate | workspace (gstack) | Root cause debugging. 4-phase methodology: Investigate → Analyze → Hypothesize → Implement. Iron Law: no fixes without root cause. |
| Retro | workspace (gstack) | Weekly engineering retrospective. Commit history, work patterns, code quality metrics, per-person contributions, trend tracking. |
| Self-Improving-Agent | workspace | Capture learnings, errors, corrections across sessions. Promotes after 3 occurrences or 7 days stable. |
| Code Review | OS plugin | Review PRs for security, performance, correctness |
| Debugging | OS plugin | Structured reproduce → isolate → diagnose → fix |
| Testing Strategy | OS plugin | Design test plans and coverage strategies |
| Architecture | OS plugin | Create and evaluate ADRs |
| System Design | OS plugin | Design services, APIs, data models |
| Deploy Checklist | OS plugin | Pre-deployment verification |
| Tech Debt | OS plugin | Identify and prioritise refactoring |

---

## 🔄 Operations

| Skill | Source | Description |
|-------|--------|------------|
| n8n-Workflow-Automation | workspace | Design robust n8n workflow JSON with idempotency, retry, error handling, human-in-the-loop queues. |
| Process Documentation | OS plugin | Flowcharts, RACI, SOPs |
| Status Report | OS plugin | KPIs, risks, action items |
| Runbook | OS plugin | Step-by-step operational procedures |
| Incident Response | OS plugin | Triage, communicate, postmortem |
| Risk Assessment | OS plugin | Identify and mitigate operational risks |

---

## 💻 IT

| Skill | Source | Description |
|-------|--------|------------|
| IPTV-Browse | workspace | Browse/search IPTV channels from iptv-org database. Country + category filters. |
| Browser-Automation | plugin | Control web pages with OpenClaw browser tool. Multi-step flows, login checks, tab management. |
| Healthcheck | bundled | Audit/harden OpenClaw hosts: SSH, firewall, updates, exposure, backups, disk encryption. |

---

## 📢 Communication

| Skill | Source | Description |
|-------|--------|------------|
| iMessage | bundled | Send/receive iMessage/SMS via macOS Messages.app CLI. |
| Apple-Notes | bundled | CRUD on Apple Notes via `memo` CLI on macOS. |
| Apple-Reminders | bundled | List/add/complete Apple Reminders via `remindctl`. |
| Brand Voice | OS plugin | Apply brand guidelines to content |
| UX Copy | OS plugin | Microcopy, error messages, CTAs |

---

## 📋 Project Management

| Skill | Source | Description |
|-------|--------|------------|
| Things-Mac | bundled | Manage Things 3 todos, inbox, projects, areas, tags on macOS. |
| Sprint Planning | OS plugin | Scope, estimate, prioritise |
| Roadmap Update | OS plugin | Reprioritise and adjust timelines |
| Stakeholder Update | OS plugin | Status reports for different audiences |

---

## 🔬 Research

| Skill | Source | Description |
|-------|--------|------------|
| Summarize | bundled | Summarize/transcribe URLs, YouTube/videos, podcasts, PDFs, articles, local files. |
| Session-Logs | bundled | Search and analyze session logs with jq. Find past decisions in older sessions. |

---

## 🌐 Integrations

| Skill | Source | Description |
|-------|--------|------------|
| GitHub | bundled | Issues, PRs, CI logs, releases, repos via `gh` CLI. Account: Arturito7ei. |
| Notion | bundled | Notion CLI/API for pages, content, data sources, comments, Workers, raw API. |
| 1Password | bundled | Secret injection via 1Password CLI (`op`). Sign-in, desktop integration. |
| X-url | bundled | Authenticated X posts, replies, DMs, search, media upload via `xurl` CLI. |

---

## 🛠️ Tools

| Skill | Source | Description |
|-------|--------|------------|
| Meme-Maker | bundled | Search meme templates and generate image memes. |
| Diagram-Maker | bundled | Create SVG/HTML or Excalidraw diagrams (concepts, architecture, flows). |
| Video-Frames | bundled | Extract frames or short clips from videos via ffmpeg. |
| TTS-Chatterbox | workspace | Local voice cloning + TTS via Chatterbox TTS (Python 3.11). Voice clone from reference audio. |
| Nano-PDF | bundled | Edit PDFs with natural-language instructions via `nano-pdf` CLI. |
| OpenAI-Whisper | bundled | Local speech-to-text with Whisper CLI. No API key required. |
| Model-Usage | bundled | Summarize Codex/Claude cost logs by model. |

---

## 🚀 7Ei-Specific (Custom)

| Skill | Source | Description |
|-------|--------|------------|
| Sprint Cycle | 7Ei_OS | Plan → execute → merge → deploy → test |
| Memory Management | 7Ei_OS | Tiered memory with promotion pipeline |
| Agent Proposal | Mission Control | LLM-generated agent profiles |
| Kronos Integration | 7Ei_OS | OpenBB data → Kronos forecasting pipeline for 7EiBank |

---

## 📦 skill-library Repo

> Physical skill implementations live in [Arturito7ei/skill-library](https://github.com/Arturito7ei/skill-library).
> Each skill package includes `SKILL.md` + `scripts/` + `.env.example`.

| Skill | Domain | Status |
|-------|--------|--------|
| jira-openclaw | Project Management | ✅ Active |

---

## ➕ Contributing a New Skill

When a new skill is created:

1. **Workspace:** Place in `~/.openclaw/workspace/skills/<name>/SKILL.md`
2. **Obsidian:** File reference note in `TARCO-MC_Vault/Skill-Library/<Category>/<name>.md`
3. **Obsidian MOC:** Add to `TARCO-MC_Vault/Skill-Library/Skill-Library.md`
4. **7Ei_OS catalog:** Update `7Ei_OS/skills/catalog.md` (PR to `Arturito7ei/7Ei_OS`)
5. **skill-library repo:** If reusable across agents, create `skill-library/<name>/SKILL.md` + PR

**Skill template:** See `skills/templates/`

---

*Maintained by: Arturito (Arturito7Ei CLAW) — Primary Agent Orchestrator of 7Ei.ai*
