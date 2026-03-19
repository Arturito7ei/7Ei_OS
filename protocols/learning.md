# Learning Protocol

## The Self-Improvement Loop

Every session makes the agent smarter. Mistakes are fuel, not failures.

```
Session N:     Human corrects agent
                   ↓
               Agent captures correction in tasks/lessons.md
                   ↓
Session N+1:   Agent reads lessons at boot → avoids same mistake
                   ↓
Consolidation: Pattern promoted to .claude/rules/ → permanent behavior
                   ↓
Session N+X:   Rule loaded automatically → mistake impossible
```

## After ANY Correction

1. Immediately update `tasks/lessons.md` with the pattern
2. Write the lesson as a rule that prevents the same mistake
3. Use imperative language: "Do X" not "The system uses X" (94% vs 73% compliance)

## Lesson Format

```markdown
## Lesson: [Short title]
- **Trigger:** What happened
- **Correction:** What the human said
- **Rule:** What to do differently (imperative)
- **Date:** When it happened
```

## Promotion Criteria

| Condition | Action |
|-----------|--------|
| Lesson triggered 3+ times | Promote to `.claude/rules/` as permanent rule |
| Lesson stable for 7+ days | Promote to `memory/long-term.md` |
| Lesson applies to all agents | Propose addition to `7Ei_OS/protocols/` |
| Lesson is project-specific | Move to project's `.claude/rules/` |

## Rule Writing Standards

- Use imperative language ("Split functions longer than 30 lines")
- One rule, one behavior — no compound rules
- Include a positive example showing the correct pattern
- Test: "Could an agent follow this rule without asking for clarification?"

## Consolidation Trigger

Run `/consolidate-memory` when:
- 5+ entries accumulated in `tasks/lessons.md`
- A session ends with significant new knowledge
- Weekly as maintenance (via `/loop` or manual)
