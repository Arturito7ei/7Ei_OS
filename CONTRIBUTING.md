# Contributing to 7Ei_OS

7Ei_OS is a **living operating system**. Agents themselves evolve it by proposing changes through pull requests.

## Who Can Contribute

Any 7Ei agent — human or AI — can propose changes. The OS improves through use.

## How Changes Originate

Most OS improvements start as lessons learned during work:

```
Session: Agent makes a mistake or discovers a pattern
    ↓
Agent records it in tasks/lessons.md
    ↓
Pattern observed 3+ times across sessions
    ↓
Agent proposes promotion to 7Ei_OS via PR
    ↓
Human or orchestrator reviews and merges
```

## Proposing a Change

### 1. Identify the change type

| Type | Example | Approval |
|------|---------|----------|
| Protocol update | New memory tier rule | Human required |
| Architecture change | New skill domain | Human required |
| Standard addition | New naming convention | Orchestrator + human |
| Integration doc | New tool setup guide | Orchestrator can merge |
| Typo / clarification | Fix wording | Auto-approved |

### 2. Create a branch and PR

```bash
git checkout -b claude/<description>-<session-id>
# Make your changes
git commit -m "os: <what changed and why>"
git push -u origin claude/<description>-<session-id>
gh pr create --title "os: <short description>" --body "<rationale>"
```

### 3. PR requirements

- **Title:** Start with `os:` prefix
- **Body:** Explain the pattern or lesson that motivated the change
- **Scope:** One concern per PR — do not bundle unrelated changes
- **Evidence:** Link to the `tasks/lessons.md` entries or sessions that surfaced the pattern

## What Belongs in 7Ei_OS

Use the boundary test before proposing a change:

**Does EVERY agent need this to function correctly?**
- YES → It belongs here (Layer 0)
- NO → It belongs in the org layer, agent identity, or project repo

Examples of what belongs:
- Memory management rules
- Workflow patterns (plan → execute → verify)
- Governance and approval tiers
- Learning and self-improvement loop
- Cross-agent coordination protocols
- Naming and coding standards that apply universally

Examples of what does NOT belong:
- Project-specific tech stack decisions → that repo's `CLAUDE.md`
- Agent personality or communication style → `agents/{instance}/AGENT.md`
- Company org chart or team structure → org layer docs
- Current tasks or blockers → session memory

## Writing Standards for OS Files

Every file in 7Ei_OS must be:

1. **Agent-consumable** — written so any LLM agent can parse and follow it without clarification
2. **Imperative** — use "Do X" not "The system does X" (94% vs 73% compliance rate)
3. **Self-contained** — each file makes sense on its own, minimal cross-references
4. **Lean** — no filler, no marketing language, every sentence earns its context-window cost
5. **Runtime-agnostic** — never assume Claude, OpenClaw, or any specific runtime

## Review Process

1. Agent opens PR with evidence from `tasks/lessons.md`
2. Orchestrator (Arturito7EiClaude) reviews for scope and consistency
3. Human approves protocol and governance changes
4. Merge to `main` — all agents inherit the update on next session

## Core Principles (Never Change Without Human Approval)

1. Simplicity first
2. No laziness — find root causes
3. Minimal impact — only touch what's necessary
4. Plan before building
5. Verify before marking done
6. Learn from mistakes
7. Protect the human
