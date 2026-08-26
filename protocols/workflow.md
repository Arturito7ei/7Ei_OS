# Workflow Protocol

## Goal-Driven Execution

Transform tasks into verifiable goals before building:

| Task phrasing | Success criteria |
|---------------|------------------|
| "Add validation" | Write tests for invalid inputs, then make them pass |
| "Fix the bug" | Write a test that reproduces it, then make it pass |
| "Refactor X" | Ensure tests pass before and after |

For multi-step tasks, state a brief plan with per-step verification:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## Plan → Execute → Verify

Every non-trivial task (3+ steps) follows this cycle.

### 1. Plan
- Enter plan mode before building
- Write detailed specs to reduce ambiguity
- Write plan to `tasks/todo.md` with checkable items
- If something goes sideways, STOP and re-plan — do not push through

### 2. Execute
- Use subagents liberally to keep main context clean
- One task per subagent for focused execution
- Offload research, exploration, and parallel analysis
- For complex problems, throw more compute at it via subagents
- Mark tasks complete as you go — do not batch

### 3. Verify
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

## Task Management

1. **Plan First** — Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan** — Check in before starting implementation
3. **Track Progress** — Mark items complete as you go
4. **Explain Changes** — High-level summary at each step
5. **Document Results** — Add review section to `tasks/todo.md`
6. **Capture Lessons** — Update `tasks/lessons.md` after corrections

## Autonomous Bug Fixing

- When given a bug report: just fix it. No hand-holding required.
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the human
- Go fix failing CI tests without being told how

## Elegance (Balanced)

- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — do not over-engineer
- Challenge your own work before presenting it
