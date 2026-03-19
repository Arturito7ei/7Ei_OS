# Memory Protocol

## Purpose

Give agents persistent memory across sessions without overloading context windows.

## Memory Tiers

```
Tier 0: Identity      → AGENT.md              Permanent. Never pruned.
Tier 1: Long-term     → memory/long-term.md   Stable facts. Grows slowly.
Tier 2: Episodic      → memory/recent.md      Rolling 48hr. Auto-pruned.
Tier 3: Working       → tasks/todo.md          Current session only.
```

## Tier Rules

### Tier 0 — Identity (Permanent)
- Agent definition (AGENT.md) and platform instructions (CLAUDE.md)
- Changed only by human or orchestrator decision
- Loaded first at every session start

### Tier 1 — Long-term (Stable Knowledge)
- Patterns, preferences, decisions, domain knowledge
- Updated via promotion from Tier 2 (not directly)
- Pruned only when contradicted by newer knowledge

### Tier 2 — Episodic (Recent Context)
- `memory/recent.md` — rolling 48hr context window
- `tasks/lessons.md` — corrections and patterns (persistent until promoted)
- Updated during and after every session

### Tier 3 — Working (Session State)
- `memory/project.md` — active workstreams and blockers
- `tasks/todo.md` — current task checklist
- Updated continuously during session

## Session Lifecycle

### Boot Sequence
1. Load `CLAUDE.md` (platform instructions)
2. Load `agents/{instance}/AGENT.md` (identity)
3. Load `.claude/rules/*` (conditional rules)
4. Load `memory/long-term.md` (stable knowledge)
5. Load `memory/project.md` (active projects)
6. Load `memory/recent.md` (last 48hrs)
7. Load `tasks/lessons.md` (corrections)

### During Session
- Update `tasks/todo.md` as work progresses
- Update `tasks/lessons.md` immediately after any user correction
- Write discoveries to `memory/recent.md`

### Session End
- Commit and push all memory changes
- Update `memory/recent.md` with session summary
- Ensure no untracked files left behind

## Promotion Rules

| Trigger | Action |
|---------|--------|
| Pattern observed 3+ times | Promote from `recent.md` → `long-term.md` |
| Fact stable for 7+ days | Promote from `recent.md` → `long-term.md` |
| Recurring mistake | Promote from `lessons.md` → `.claude/rules/` |
| Architectural decision | Record in project's ADR or Obsidian vault |

## Pruning Rules

| Condition | Action |
|-----------|--------|
| Entry > 48hr AND promoted | Archive (remove from `recent.md`) |
| Entry > 7 days AND never promoted | Remove |
| Contradicted by newer knowledge | Update or remove |
| Session state from completed task | Clear from `project.md` |

## Consolidation

Run `/consolidate-memory` periodically:
1. Scan `recent.md` and `lessons.md` for promotable patterns
2. Promote stable knowledge to `long-term.md`
3. Prune stale entries from `recent.md`
4. Update `project.md` (archive completed workstreams)
5. Propose new `.claude/rules/` if a lesson recurs 3+ times

## Cross-Agent Memory

Agents share memory via:
- **Git** — `memory/` directory in the shared agent repo (source of truth)
- **Obsidian Sync** — real-time vault synchronization
- **Task handoff files** — `platform/coordination/tasks/*.yaml`

Each agent reads shared memory but writes to its own section or files to avoid conflicts.
