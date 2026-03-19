# Knowledge Layers — Quick Reference

## The 5 Layers

| Layer | Name | Scope | Example | Changes |
|-------|------|-------|---------|---------|
| L0 | OS | All agents | "Plan before building" | Rarely |
| L1 | Organization | All of 7Ei | "We use Jira project O7MC" | Monthly |
| L2 | Agent Identity | One agent | "I'm direct and Swiss-German" | Per session |
| L3 | Project | One codebase | "Use T tokens for colors" | Per sprint |
| L4 | Session | Right now | "Blocked on API auth" | Continuously |

## Shared vs Individual Knowledge

```
SHARED (all agents read)          INDIVIDUAL (one agent owns)
─────────────────────────         ──────────────────────────
L0: Protocols                     L2: Identity & personality
L1: Org structure                 L2: Personal lessons
L1: Tool config (Jira keys)       L2: Skill subset
L1: Brand guidelines              L3: Project context (when sole dev)
L3: Project ADRs (when team)      L4: Current task state
```

## What Gets Loaded When

```
ALWAYS LOADED (every session, every repo):
  ├── L0: 7Ei_OS protocols (via CLAUDE.md reference or .claude/rules/)
  ├── L1: Org facts (via memory/long-term.md)
  └── L2: Agent identity (via AGENT.md)

LOADED PER REPO:
  └── L3: Project context (via that repo's CLAUDE.md + .claude/rules/)

LOADED PER SESSION:
  ├── L4: memory/recent.md
  ├── L4: memory/project.md
  └── L4: tasks/todo.md + tasks/lessons.md
```

## Finding Similar Principles Across Layers

When knowledge appears in multiple places, consolidate upward:

1. Same rule in 3+ project repos → promote to L1 (org standard)
2. Same lesson for 2+ agents → promote to L1 or L0
3. Same pattern across all projects → promote to L0 (protocol)

Use `/consolidate-memory` to detect these patterns automatically.
