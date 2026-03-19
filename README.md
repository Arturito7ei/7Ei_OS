# 7Ei_OS — Agent Operating System

The shared brain for all 7Ei agents. Runtime-agnostic protocols for memory, knowledge, workflow, and governance.

## What This Is

7Ei_OS is the foundational layer that every 7Ei agent inherits — whether running on Claude Code, OpenClaw, or any future runtime. It defines **how agents think**, not **what they think about**.

## Architecture

```
7Ei_OS/
├── README.md                     ← You are here
├── ARCHITECTURE.md               ← Knowledge layer model (start here)
├── protocols/                    ← Shared brain (all agents inherit)
│   ├── memory.md                 ← 4-tier memory system
│   ├── knowledge-boundaries.md   ← What knowledge goes where
│   ├── workflow.md               ← Plan, execute, verify
│   ├── learning.md               ← Self-improvement loop
│   ├── principles.md             ← Core operating principles
│   └── governance.md             ← Approval tiers, audit
├── identity/                     ← How to define an agent
│   ├── template.md               ← Agent identity blueprint
│   └── knowledge-card.md         ← Per-agent knowledge manifest
├── knowledge/                    ← Knowledge classification
│   ├── layers.md                 ← The 5-layer knowledge model
│   └── sync.md                   ← Cross-agent knowledge sync
└── bootstrap/                    ← Quick-start for new agents
    └── onboarding.md             ← First-session checklist
```

## How To Use

**For a new agent:** Read `bootstrap/onboarding.md`, then `ARCHITECTURE.md`.

**For an existing agent:** Reference `protocols/` as your operating manual. Your repo's `CLAUDE.md` should be thin — point to these protocols, don't duplicate them.

**For a new project repo:** Copy `bootstrap/onboarding.md` into your repo as `.claude/rules/7ei-os.md` and customize the project layer only.

## Design Principles

- **Write once, inherit everywhere** — protocols live here, not in each repo
- **Separate identity from protocol** — who you are ≠ how you work
- **Separate knowledge from memory** — what you know ≠ how you remember
- **Runtime-agnostic** — works for Claude Code, OpenClaw, or any LLM agent
- **Hyper-efficient** — every file earns its context window cost
