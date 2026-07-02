# Coordination Protocol

How 7Ei agents work together without stepping on each other.

## Active Agents

| Agent | Runtime | Capabilities | Primary Repos |
|-------|---------|-------------|---------------|
| Arturito7EiClaude | Claude Code | Code, architecture, orchestration, planning | All repos |
| Arturito7EiClaw | OpenClaw + Telegram | Browser, Telegram, Jira, GitHub actions | skill-library, coordination tasks |

## Task Handoff

**Primary channel: Mission Control** (`https://7ei-backend.fly.dev`, agent API). MC provides what the YAML files approximated, hardened: atomic task checkout (CAS claim — exactly one owner), dependencies (`blocked_by` gates claims), run telemetry + resumable session state, unified timeline (comments/attachments/runs), approval gates, and heartbeats. Agents interact via their agent token:

```
GET  /api/agent/tasks?state=assigned   → what's mine?
POST /api/agent/tasks/:id/claim        → atomic claim (one winner)
POST /api/agent/tasks/:id/result       → output + done|failed
POST /api/agent/tasks/:id/comment      → progress notes on the timeline
POST /api/agent/heartbeat              → green|amber liveness
```

**Fallback channel** (MC unreachable, or work outside MC's scope): YAML files in `platform/coordination/tasks/`:

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
| Mission Control (agent API + Cockpit) | Task handoff, heartbeats, approvals, run telemetry — PRIMARY | All agents |
| `platform/coordination/tasks/` | Task handoff (YAML) — fallback when MC unavailable | All agents |
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
1. **`POST /api/agent/heartbeat`** (green/amber) — MC's heartbeat engine tracks staleness and surfaces it in the Cockpit (primary)
2. Git commits (natural heartbeat)
3. Task status updates (MC timeline, or YAML fallback)
4. Memory updates in the vault (`Memory/agents/<agent>/recent.md`)

If an agent's MC heartbeat goes stale on an active task, the orchestrator should check status.

## Escalation

| Situation | Action |
|-----------|--------|
| Task blocked for 4+ hours | Mark task blocked in MC (comment with reason), notify orchestrator |
| Action needs human approval | MC approval request (auto-created by execution policies) — human decides in Cockpit |
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
