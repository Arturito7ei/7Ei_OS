# Coordination Protocol

How 7Ei agents work together without stepping on each other.

## Active Agents

| Agent | Runtime | Capabilities | Primary Repos |
|-------|---------|-------------|---------------|
| Arturito7EiClaude | Claude Code | Code, architecture, orchestration, planning | All repos |
| Arturito7EiClaw | OpenClaw + Telegram | Browser, Telegram, Jira, GitHub actions | skill-library, coordination tasks |

## Task Handoff

Agents coordinate via YAML files in `platform/coordination/tasks/`:

```yaml
# platform/coordination/tasks/TASK-001.yaml
id: TASK-001
title: "Create Jira board for Sprint 1"
created_by: arturito7eiclaude
assigned_to: arturito7eiclaw
status: pending  # pending | in_progress | done | blocked
priority: high
context: |
  We need the O7MC Jira board populated with sprint tasks.
  Use jira-openclaw skill from skill-library.
deliverables:
  - Jira board created with sprint tasks
  - Task keys reported back
created_at: "2026-03-19T00:00:00Z"
```

### Handoff Rules

1. **One owner per task** — never assign a task to multiple agents
2. **Include full context** — the receiving agent has no shared memory of your session
3. **Define deliverables** — what does "done" look like?
4. **Update status** — mark `in_progress` when you start, `done` when finished
5. **Report back** — add a `result` field with outcomes when completing

### Status Flow

```
pending → in_progress → done
                ↓
             blocked → (reassign or escalate)
```

## Communication Channels

| Channel | Use For | Agents |
|---------|---------|--------|
| `platform/coordination/tasks/` | Task handoff (YAML) | All agents |
| Git commits and PRs | Code changes, reviews | All agents |
| Obsidian vault (Open7Ei_ObsidianVault) | Shared knowledge, research | Claude + Claw |
| Telegram | Human notifications, quick updates | Claw → Human |
| Jira (O7MC project) | Sprint tracking, backlog | All agents |

## Conflict Prevention

- Each agent works on assigned repos/tasks — check handoff files before starting
- If two agents need the same file, coordinate via task handoff first
- Git branches prevent code conflicts — each agent uses its own branch prefix
- Memory files: each agent writes to its own section, reads shared sections

## Heartbeat Pattern

Agents signal activity through:
1. Git commits (natural heartbeat)
2. Task status updates in `platform/coordination/tasks/`
3. Memory updates in `memory/recent.md`

If an agent hasn't committed in 24 hours on an active task, the orchestrator should check status.

## Escalation

| Situation | Action |
|-----------|--------|
| Task blocked for 4+ hours | Flag in handoff file, notify orchestrator |
| Agent capabilities insufficient | Reassign to agent with right tools |
| Cross-agent conflict | Orchestrator decides, documents in lessons |
| Human decision needed | Mark task blocked, notify via Telegram |

## Shared Resources

### Skill Library (`Arturito7ei/skill-library`)
- Shared skills usable by any agent
- Each skill has a `SKILL.md` with instructions and `scripts/` with helpers
- Agents contribute new skills via PR
- Current skills: `jira-openclaw` (contributed by Arturito7EiClaw)

### Obsidian Vaults
- **Open7EiMc** — Mission Control planning and data
- **Open7Ei_ObsidianVault** — Collaboration vault shared between agents
