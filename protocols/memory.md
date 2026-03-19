# Memory Protocol

Persistent memory across sessions without overloading context windows.

## 4 Tiers

```
Tier 0: Identity      → AGENT.md              Permanent. Never pruned.
Tier 1: Long-term     → memory/long-term.md   Stable facts. Grows slowly.
Tier 2: Episodic      → memory/recent.md      Rolling 48hr window. Auto-pruned.
Tier 3: Working       → tasks/todo.md          Current session only.
```

## Tier Rules

### Tier 0 — Identity (Permanent)
- `AGENT.md` defines who you are — name, role, personality, skills
- `CLAUDE.md` defines project-level instructions
- Changed only by human or orchestrator decision
- Load first at every session start

### Tier 1 — Long-term (Stable Knowledge)
- Patterns, preferences, architectural decisions, domain knowledge
- Updated via promotion from Tier 2 — never written directly
- Prune only when contradicted by newer knowledge
- File: `memory/long-term.md`

### Tier 2 — Episodic (Recent Context)
- `memory/recent.md` — rolling 48-hour context window
- `tasks/lessons.md` — corrections and patterns (persistent until promoted)
- Update during and after every session

### Tier 3 — Working (Session State)
- `memory/project.md` — active workstreams and blockers
- `tasks/todo.md` — current task checklist
- Update continuously during session
- Clear completed workstreams at session end

## Promotion Rules

| Trigger | Action |
|---------|--------|
| Pattern observed 3+ times | Promote from `recent.md` → `long-term.md` |
| Fact stable for 7+ days | Promote from `recent.md` → `long-term.md` |
| Recurring mistake (3+ times) | Promote from `lessons.md` → `.claude/rules/` |
| Architectural decision | Record in project ADR or Obsidian vault |
| Universal pattern across agents | Propose addition to `7Ei_OS/protocols/` via PR |

## Pruning Rules

| Condition | Action |
|-----------|--------|
| Entry older than 48hr AND already promoted | Remove from `recent.md` |
| Entry older than 7 days AND never promoted | Remove |
| Contradicted by newer knowledge | Update or remove |
| Session state from completed task | Clear from `project.md` |

## File Locations

All memory files live in the agent's identity repo (e.g., `Arturito7ei/Arturito7ei`):

```
memory/
├── long-term.md     # Tier 1 — stable knowledge
├── recent.md        # Tier 2 — rolling 48hr context
└── project.md       # Tier 3 — active workstreams

tasks/
├── todo.md          # Tier 3 — current session tasks
└── lessons.md       # Tier 2 — corrections and patterns
```

## Cross-Agent Memory

Agents share knowledge via:
- **Git** — `memory/` directory in the shared agent repo (source of truth)
- **Obsidian Sync** — real-time vault synchronization
- **Task handoff files** — `platform/coordination/tasks/*.yaml`

Each agent reads shared memory but writes to its own section or files to avoid conflicts.

## Consolidation

Run periodically (weekly or when 5+ entries accumulate in `lessons.md`):

1. Scan `recent.md` and `lessons.md` for promotable patterns
2. Promote stable knowledge to `long-term.md`
3. Prune stale entries from `recent.md`
4. Archive completed workstreams from `project.md`
5. Propose new `.claude/rules/` entries if a lesson recurs 3+ times
6. Commit and push all memory changes
