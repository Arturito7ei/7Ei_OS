# Knowledge Sync Protocol

## The Problem

7Ei_OS protocols (L0) live in one repo but must be followed in all repos. How do we keep them in sync without submodules?

## Sync Strategy: Reference + Embed

### Option A: Reference (Recommended for Claude Code)

Each repo's `CLAUDE.md` references 7Ei_OS but doesn't copy it:

```markdown
## Operating System
Follow all protocols from 7Ei_OS (github.com/Arturito7ei/7Ei_OS).
Key protocols: memory, workflow, learning, principles, governance.
```

The agent reads 7Ei_OS at session start if available, otherwise relies on the embedded summary in `CLAUDE.md`.

### Option B: Embed Minimal (For repos without 7Ei_OS access)

Copy a minimal protocol summary into `.claude/rules/7ei-os-core.md`:

```markdown
# 7Ei OS Core (synced from 7Ei_OS — do not edit directly)
# Last sync: {date}

## Memory: 4 tiers (identity → long-term → episodic → working)
## Workflow: Plan → Execute → Verify
## Learning: Correction → lesson → rule promotion
## Principles: Simplicity, No laziness, Minimal impact, Verify before done
## Governance: Auto/Orchestrator/Human approval tiers
```

### Option C: Submodule (For CI/CD environments)

Mount 7Ei_OS as a git submodule at `.7ei-os/`:

```bash
git submodule add https://github.com/Arturito7ei/7Ei_OS.git .7ei-os
```

## Sync Frequency

| Layer | Sync Method | Frequency |
|-------|------------|-----------|
| L0 (OS) | Git pull or API fetch | Weekly or on protocol change |
| L1 (Org) | Obsidian Sync + Git | Real-time (Obsidian) or daily (Git) |
| L2 (Agent) | Agent repo push | Per session |
| L3 (Project) | In-repo, no sync needed | N/A |
| L4 (Session) | In-repo, no sync needed | N/A |

## Drift Detection

During `/consolidate-memory`, check:
1. Does this repo's `.claude/rules/7ei-os-core.md` match current 7Ei_OS?
2. Are there project rules that should be promoted to L0 or L1?
3. Are there L0 rules being overridden at L3 without justification?

Flag drift in `tasks/lessons.md` for human review.
