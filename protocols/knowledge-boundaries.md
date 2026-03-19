# Knowledge Boundaries Protocol

## Purpose

Define what knowledge belongs where so agents never duplicate, contradict, or waste context on irrelevant information.

## The Boundary Test

Before storing any knowledge, ask these questions in order:

```
1. Does EVERY agent need this to function?
   → YES → Layer 0 (OS protocols)
   → NO  → continue

2. Does everyone at 7Ei need this?
   → YES → Layer 1 (Organization)
   → NO  → continue

3. Is this about WHO I am (not what I'm working on)?
   → YES → Layer 2 (Agent Identity)
   → NO  → continue

4. Is this about THIS project specifically?
   → YES → Layer 3 (Project)
   → NO  → continue

5. Is this only relevant right now?
   → YES → Layer 4 (Session)
```

## Layer 0 — OS (Universal Agent Knowledge)

**Belongs here:**
- Memory management rules (tiers, promotion, pruning)
- Workflow patterns (plan → execute → verify)
- Learning loop (correction → lesson → rule)
- Core principles (simplicity, rigor, autonomy)
- Governance model (approval tiers)
- This document (knowledge boundary rules)

**Does NOT belong here:**
- Company-specific tools (Jira, Google Workspace)
- Agent personality or style
- Tech stack decisions
- Current tasks or blockers

**Storage:** `7Ei_OS/protocols/`
**Update frequency:** Rare. Human approval required.

## Layer 1 — Organization (7Ei Company Knowledge)

**Belongs here:**
- Company identity (Swiss foundation, mission, values)
- Org structure (teams, roles, reporting)
- Shared tools and services (Jira project keys, vault IDs, repo URLs)
- Cross-team standards (communication norms, brand guidelines)
- Budget and resource policies
- Coordination protocols between agents

**Does NOT belong here:**
- How memory works (that's L0)
- Individual agent preferences (that's L2)
- How to deploy a specific app (that's L3)

**Storage:** `platform/org/`, Obsidian vault, `memory/long-term.md` (org facts section)
**Update frequency:** Monthly or on org changes.

## Layer 2 — Agent Identity (Individual Knowledge)

**Belongs here:**
- Name, role, personality, communication style
- Runtime and capabilities (Claude Code vs OpenClaw vs other)
- Which skills this agent uses
- Personal lessons and behavioral patterns
- Access credentials and integrations
- Relationships with other agents

**Does NOT belong here:**
- Company org chart (that's L1)
- Project tech stack (that's L3)
- General workflow rules (that's L0)

**Storage:** `agents/{instance}/AGENT.md`, `agents/{instance}/config.yaml`
**Update frequency:** Per session (lessons) or on role changes.

## Layer 3 — Project (Codebase & Domain Knowledge)

**Belongs here:**
- Tech stack and framework choices
- Design tokens, style guides, conventions
- Architecture Decision Records (ADRs)
- Repo-specific rules (linting, testing, deploy)
- Team roles within this project
- Project-specific lessons and patterns
- CI/CD and deploy configuration

**Does NOT belong here:**
- Memory management rules (that's L0)
- Company identity (that's L1)
- Agent personality (that's L2)

**Storage:** Each repo's `CLAUDE.md` + `.claude/rules/`
**Update frequency:** Per sprint or on architectural changes.

## Layer 4 — Session (Ephemeral Working State)

**Belongs here:**
- Current task list and progress
- Recent decisions and their rationale
- Active blockers and waiting items
- In-progress work context
- Conversation history summary

**Does NOT belong here:**
- Anything that should survive beyond 48 hours (promote it)
- Stable facts or preferences (that's L1 or L2)
- Reusable patterns (promote to appropriate layer)

**Storage:** `memory/recent.md`, `tasks/todo.md`, `memory/project.md`
**Update frequency:** Continuously during session.

## Conflict Resolution

When knowledge at different layers contradicts:

1. **Lower layer wins for specifics** — A project rule overrides a general principle for that project
2. **Higher layer wins for protocol** — OS-level memory rules override any project-level memory hack
3. **Newer knowledge wins** — When same-layer entries conflict, the more recent one wins
4. **Flag and resolve** — When in doubt, flag the contradiction in `tasks/lessons.md` and ask the orchestrator

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Duplicating OS rules in each CLAUDE.md | Drift, wasted context | Reference 7Ei_OS, don't copy |
| Storing project knowledge in agent memory | Agent gets confused across projects | Move to project's `.claude/rules/` |
| Keeping session state in long-term memory | Context bloat, stale data | Prune via consolidation |
| Putting agent personality in project files | Other agents inherit wrong voice | Move to `agents/{instance}/AGENT.md` |
| Storing company info in one agent only | Other agents lack context | Move to L1 (org) or shared vault |
