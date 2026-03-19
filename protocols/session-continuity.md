# Session Continuity Protocol

How agents boot, maintain state during work, and hand off cleanly between sessions.

## The Problem

AI agents lose all memory between sessions. Without a continuity protocol, every session starts from zero — wasting time re-learning context and repeating mistakes.

## Boot Sequence

Load files in this exact order at session start:

```
1. CLAUDE.md                    → Platform instructions (Layer 3)
2. agents/{instance}/AGENT.md   → Identity — who am I? (Layer 2)
3. .claude/rules/*              → Conditional rules (Layer 3)
4. memory/long-term.md          → Stable knowledge (Tier 1)
5. memory/project.md            → Active workstreams (Tier 3)
6. memory/recent.md             → Last 48hrs context (Tier 2)
7. tasks/lessons.md             → Corrections and patterns (Tier 2)
```

After loading, confirm context by stating:
- What you're working on (from `project.md`)
- Any active blockers (from `recent.md`)
- Key lessons to remember (from `lessons.md`)

## During Session

### Continuous Updates
- Update `tasks/todo.md` as work progresses — mark tasks complete immediately, not in batches
- Write corrections to `tasks/lessons.md` immediately after any human correction
- Log discoveries and decisions to `memory/recent.md`

### Lesson Format
When recording a correction:

```markdown
## Lesson: [Short title]
- **Trigger:** What happened
- **Correction:** What the human said
- **Rule:** What to do differently (imperative voice)
- **Date:** YYYY-MM-DD
```

### Decision Format
When recording a significant decision:

```markdown
## Decision: [Short title]
- **Context:** Why this came up
- **Choice:** What was decided
- **Rationale:** Why this option over alternatives
- **Date:** YYYY-MM-DD
```

## Session End

Before ending a session:

1. **Update `memory/recent.md`** with a session summary:
   ```markdown
   ## Session: YYYY-MM-DD
   - **Focus:** What was worked on
   - **Completed:** What got done
   - **Blockers:** What's still stuck
   - **Next:** What should happen next session
   ```

2. **Commit and push all memory changes** — memory files must be in version control

3. **Update task handoff files** if other agents need to pick up work

4. **Verify no untracked files** are left behind

## Consolidation

Run when 5+ entries accumulate in `lessons.md` or weekly:

1. **Scan** `recent.md` and `lessons.md` for promotable patterns
2. **Promote** stable knowledge to `long-term.md` (pattern seen 3+ times or stable 7+ days)
3. **Prune** stale entries from `recent.md` (older than 48hr and already promoted)
4. **Archive** completed workstreams from `project.md`
5. **Propose** new `.claude/rules/` entries if a lesson recurs 3+ times
6. **Commit** all changes

## Handoff Between Agents

When one agent hands work to another:

1. Create a task handoff file in `platform/coordination/tasks/`
2. Include full context — the receiving agent has no memory of your session
3. Reference relevant `memory/recent.md` entries if needed
4. Define clear deliverables and acceptance criteria

## Recovery From Context Loss

If you wake up with no memory files:

1. Read `AGENT.md` and `CLAUDE.md` — establish identity
2. Check `git log` — what was the last session's work?
3. Read any `memory/` files that exist — rebuild context
4. Read `tasks/lessons.md` — don't repeat past mistakes
5. If files are missing, state what you know and ask the human for context

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Skipping boot sequence | Missing context, repeated mistakes | Always load all 7 files |
| Batching task completions | User can't track progress | Mark complete immediately |
| Not writing session summary | Next session starts blind | Always write before ending |
| Copying memory verbatim between agents | Context pollution | Use task handoff files instead |
| Keeping session state in long-term | Memory bloat | Prune via consolidation |
