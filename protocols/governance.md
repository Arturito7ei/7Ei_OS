# Governance Protocol

What agents can do autonomously, what needs approval, and how decisions are audited.

## Approval Tiers

### Tier 1 — Auto-Approved (No Confirmation Needed)

- Read files, search code, explore repos
- Edit code in feature branches
- Run tests and builds
- Research queries (web search, documentation)
- Update own memory files (Tiers 2-4)
- Internal agent communication (task handoff files)
- Create feature branches

### Tier 2 — Orchestrator Approval

- External API calls with side effects
- Budget reallocation between projects
- Spawning new agent instances
- Cross-project resource sharing
- Promoting knowledge to Layer 0 or Layer 1
- Modifying shared configuration files
- Installing new dependencies

### Tier 3 — Human Approval Required

- Destructive operations (delete, force-push, reset)
- External communications (email, social media, PR comments on public repos)
- Financial transactions of any kind
- Governance rule changes (this file)
- Publishing or deploying to production
- Changes to 7Ei_OS protocols
- Merging to `main` on critical repos
- Creating or modifying access credentials
- Any action that cannot be reversed

## Decision Framework

When unsure about approval tier, ask:

```
Can this action be undone easily?
  → YES → Likely Tier 1
  → NO  → Continue

Does this affect only my local environment?
  → YES → Tier 1
  → NO  → Continue

Does this affect other agents or shared state?
  → YES → Tier 2 (orchestrator)
  → NO  → Continue

Does this affect humans, money, or production?
  → YES → Tier 3 (human)
```

## Audit Trail

All significant actions are logged across:

| What | Where | Retention |
|------|-------|-----------|
| Session decisions | `memory/recent.md` | 48 hours (rolling) |
| Corrections and patterns | `tasks/lessons.md` | Until promoted |
| Code changes | Git history | Permanent |
| Knowledge updates | Obsidian vault | Permanent |
| Task handoffs | `platform/coordination/tasks/` | Until archived |

## Budget Controls

- Each project has a defined resource budget (tokens, API calls, compute)
- Agents track spend against budget
- 80% threshold → warning to orchestrator
- 100% threshold → hard stop, requires human override
- Monthly reset with configurable rollover

## Core Principles (Immutable Without Human Approval)

1. **Simplicity first** — minimal code impact, every change as simple as possible
2. **No laziness** — find root causes, no temporary fixes, senior developer standards
3. **Minimal impact** — only touch what's necessary, avoid introducing bugs
4. **Plan before building** — enter plan mode for any non-trivial task (3+ steps)
5. **Verify before done** — never mark complete without proving it works
6. **Learn from mistakes** — update `tasks/lessons.md` after any correction
7. **Protect the human** — confirm before irreversible actions, flag security risks immediately
