# 7Ei_OS — Agent Operating System

The living operating system for all 7Ei agents. Runtime-agnostic. LLM-agnostic. This is Layer 0 — the foundation everything else builds on.

## What This Is

7Ei_OS defines **how agents operate**, not what they work on. Any new agent — Claude, Gemini, GPT, open-source — reads this repo and immediately knows how to think, remember, coordinate, and improve within the 7Ei ecosystem.

## Quick Start

**New agent?** Read these in order:
1. `protocols/memory.md` — how you remember
2. `protocols/session-continuity.md` — how you boot and shut down
3. `protocols/governance.md` — what you can and cannot do autonomously
4. `architecture/agent-template.md` — the DNA you inherit
5. `standards/naming.md` — how you're named

**New project repo?** Add a thin `CLAUDE.md` that references this OS:
```markdown
## Operating System
Follow all protocols defined in Arturito7ei/7Ei_OS.
```

## Structure

```
7Ei_OS/
├── README.md                       # You are here
├── CHANGELOG.md                    # OS evolution log
├── CONTRIBUTING.md                 # How agents propose OS changes
├── protocols/
│   ├── memory.md                   # 4-tier memory architecture
│   ├── coordination.md             # Multi-agent coordination and task handoff
│   ├── governance.md               # Approval tiers (auto/orchestrator/human)
│   ├── spawning.md                 # Creating new agents from the template
│   └── session-continuity.md       # Boot, consolidation, handoff between sessions
├── architecture/
│   ├── agent-template.md           # Arturito7EiT DNA — what every agent inherits
│   ├── agent-hierarchy.md          # Template → instances → specialized agents
│   ├── skill-system.md             # Skill domains, composability, the skill library
│   └── knowledge-graph.md          # Obsidian vault integration, research pipeline
├── standards/
│   ├── code-review.md              # Code review checklist
│   ├── naming.md                   # Agent and entity naming conventions
│   └── repo-conventions.md         # Repo defaults, branch naming, commit style
└── integrations/
    ├── obsidian.md                 # Vault structure, MCP, Obsidian Sync
    ├── jira.md                     # 7ei.atlassian.net, O7MC project space
    ├── github.md                   # Repo map, permissions, automation
    └── google-workspace.md         # Docs, Sheets, Drive, Gmail, Calendar
```

## Design Principles

- **Write once, inherit everywhere** — protocols live here, not duplicated per repo
- **Agent-consumable** — every file is written for agents to parse and follow, not just humans to read
- **Runtime-agnostic** — works for Claude Code, OpenClaw, GPT, Gemini, or any future LLM agent
- **Living system** — agents themselves propose improvements via PR (see `CONTRIBUTING.md`)
- **Hyper-efficient** — every file earns its context-window cost

## Active Agent Instances

| Agent | Runtime | Role | Status |
|-------|---------|------|--------|
| Arturito7EiClaude | Claude Code | Master Orchestrator, Chief of Staff | Active |
| Arturito7EiClaw | OpenClaw + Telegram | Operations, Browser + Jira + GitHub | Active |

## Repository

- **Org:** [Arturito7ei](https://github.com/Arturito7ei)
- **Visibility:** Private
- **Owner:** arturito@7ei.ai
