# 7Ei_OS — Agent Operating System

The living operating system for all 7Ei agents. Runtime-agnostic. LLM-agnostic. This is Layer 0 — the foundation everything else builds on.

## What This Is

7Ei_OS defines **how agents operate**, not what they work on. Any new agent — Buzz, Grok, Claude, Hermes, or a future runtime — reads this repo and immediately knows how to think, remember, coordinate, and improve within the 7Ei ecosystem.

## Quick Start

**New or swapped agent?** Read [`bootstrap/CATCH_UP.md`](bootstrap/CATCH_UP.md) first, then the files it lists, in that order.

**New project repo?** Add a thin `CLAUDE.md` that references this OS:
```markdown
## Operating System
Follow all protocols defined in Arturito7ei/7Ei_OS.
Shared knowledge: vault Arturito7ei/7Ei-MC_TARCO.
```

## Structure

```
7Ei_OS/
├── README.md                       # You are here
├── bootstrap/CATCH_UP.md           # Mandatory first-read (any runtime)
├── onboarding/                     # Join path + runtime adapters
├── blueprints/                     # Orchestration index
├── CHANGELOG.md                    # OS evolution log
├── CONTRIBUTING.md                 # How agents propose OS changes
├── protocols/                      # Memory, coordination, governance, …
├── architecture/                   # Template, hierarchy, skills, knowledge graph
├── standards/                      # Review, naming, repo conventions
├── integrations/                   # Vault, GitHub, Jira, Google, …
├── agents/                         # Instance profiles (may lag L1)
└── skills/                         # Catalog + SKILL.md library
```

## Design Principles

- **Write once, inherit everywhere** — protocols live here, not duplicated per repo
- **Agent-consumable** — every file is written for agents to parse and follow, not just humans to read
- **Runtime-agnostic** — works for Buzz, Arturita/Grok, Claude Code, OpenClaw, Hermes, or any future agent
- **Living system** — agents themselves propose improvements via PR (see `CONTRIBUTING.md`)
- **Hyper-efficient** — every file earns its context-window cost

## Runtimes

L0 pointer to current reality. L1 seats (`7man`, `7rd`, `7ops`, `7dev`, `7fin`, `7mkt`) live in the TARCO vault — this table is not the org chart. Do not mark a runtime Active unless listed below.

| Runtime | Adapter | Role | Status |
|---------|---------|------|--------|
| Buzz | `onboarding/runtimes/buzz.md` | Primary GitHub producer (Mac mini) | **Active (primary)** |
| Arturita (Grok Bot) | `onboarding/runtimes/arturita.md` | Remote GitHub + vault partner | **Active** |
| Claude Code | `onboarding/runtimes/claude-code.md` | Code execution, work orders | **Active** |
| OpenClaw | `onboarding/runtimes/openclaw.md` | Ops, browser, Telegram, Jira | **Secondary / parked** (vault namespace legacy read-only) |
| Hermes | `onboarding/runtimes/hermes.md` | Generic HTTPS/bearer join | **Planned / available** |

Paperclip/TARCO control-plane agents: `integrations/paperclip.md` + vault `07-Agents/`.

## Repository

- **Org:** [Arturito7ei](https://github.com/Arturito7ei)
- **Visibility:** Private
- **Owner:** arturito@7ei.ai
- **L1 vault:** [Arturito7ei/7Ei-MC_TARCO](https://github.com/Arturito7ei/7Ei-MC_TARCO)
