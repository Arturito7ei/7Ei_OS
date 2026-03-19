# 7Ei_OS — Knowledge Architecture

## The Problem

Agents accumulate knowledge across sessions, projects, and roles. Without clear boundaries, knowledge gets duplicated, contradicts itself, or loads into context when irrelevant — wasting tokens and causing confusion.

## The 5-Layer Knowledge Model

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  LAYER 0: OPERATING SYSTEM (7Ei_OS)                 UNIVERSAL   │
│  ─────────────────────────────────────                          │
│  Scope: ALL agents, ALL repos, ALL projects                     │
│  Changes: Rarely. Requires human approval.                      │
│                                                                 │
│  • Memory protocol (tiers, promotion, pruning)                  │
│  • Workflow protocol (plan → execute → verify)                  │
│  • Learning protocol (correction → lesson → rule)               │
│  • Core principles (simplicity, rigor, autonomy)                │
│  • Governance model (approval tiers, audit)                     │
│  • Knowledge boundary rules (this document)                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LAYER 1: ORGANIZATION (7Ei)                     COMPANY-WIDE   │
│  ─────────────────────────────────                              │
│  Scope: All 7Ei agents and humans                               │
│  Changes: Monthly. Orchestrator or human approval.              │
│                                                                 │
│  • Company identity (Swiss foundation, EQ+IQ+AI)                │
│  • Org structure (teams, roles, services)                       │
│  • Shared knowledge base (Obsidian vault)                       │
│  • Cross-agent coordination (task handoff, heartbeat)           │
│  • Tool integrations (Jira, Google, Obsidian)                   │
│  • Budget and resource allocation                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LAYER 2: AGENT IDENTITY                          PER-AGENT     │
│  ─────────────────────────────────                              │
│  Scope: ONE agent instance                                      │
│  Changes: Per session. Agent can self-update.                   │
│                                                                 │
│  • Name, role, personality, voice                               │
│  • Runtime & capabilities (Claude Code / OpenClaw / other)      │
│  • Skill subset (which skills I use)                            │
│  • Communication style & preferences                            │
│  • Personal memory (my lessons, my patterns)                    │
│  • Integrations I have access to                                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LAYER 3: PROJECT / DEPARTMENT                    PER-PROJECT   │
│  ─────────────────────────────────                              │
│  Scope: ONE project, product, or department                     │
│  Changes: Per sprint. Team members update.                      │
│                                                                 │
│  • Tech stack & conventions                                     │
│  • Architecture decisions (ADRs)                                │
│  • Project-specific rules & standards                           │
│  • Team composition & roles in this project                     │
│  • Project memory (decisions, blockers, context)                │
│  • Deploy & CI/CD config                                        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LAYER 4: SESSION (Working Memory)                EPHEMERAL     │
│  ─────────────────────────────────                              │
│  Scope: ONE work session                                        │
│  Changes: Continuously. Auto-managed.                           │
│                                                                 │
│  • Current task list (todo.md)                                  │
│  • Recent context (last 48hr rolling)                           │
│  • Active decisions and blockers                                │
│  • In-progress work state                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Knowledge Flow

```
        ┌──────────┐
        │ Session  │ ← Ephemeral. Created and consumed within hours.
        │ (L4)     │
        └────┬─────┘
             │ correction or pattern detected
             ▼
        ┌──────────┐
        │ Agent    │ ← Agent learns. Lesson added to personal memory.
        │ (L2)     │
        └────┬─────┘
             │ pattern seen 3+ times OR stable 7+ days
             ▼
        ┌──────────┐
        │ Project  │ ← If project-specific, stays here.
        │ (L3)     │   If universal, promotes further.
        └────┬─────┘
             │ pattern applies across projects
             ▼
        ┌──────────┐
        │ Org      │ ← Company-wide knowledge. All agents benefit.
        │ (L1)     │
        └────┬─────┘
             │ fundamental protocol change
             ▼
        ┌──────────┐
        │ OS       │ ← Rare. Changes how all agents operate.
        │ (L0)     │
        └──────────┘
```

## Decision Tree: Where Does This Knowledge Belong?

```
Is it about HOW agents work (memory, workflow, learning)?
  → YES → Layer 0 (OS)

Is it about 7Ei the company (org, teams, services, tools)?
  → YES → Layer 1 (Organization)

Is it about WHO this specific agent is (name, style, skills)?
  → YES → Layer 2 (Agent Identity)

Is it about THIS codebase or project (tech stack, rules, ADRs)?
  → YES → Layer 3 (Project)

Is it about what's happening RIGHT NOW (tasks, recent context)?
  → YES → Layer 4 (Session)
```

## File Mapping

| Layer | Where It Lives | Loaded When |
|-------|---------------|-------------|
| L0: OS | `7Ei_OS/protocols/` | Always (via CLAUDE.md reference) |
| L1: Org | `platform/org/`, Obsidian vault | Always |
| L2: Agent | `agents/{instance}/AGENT.md`, `memory/long-term.md` | Always |
| L3: Project | Each repo's `CLAUDE.md` + `.claude/rules/` | When working on that repo |
| L4: Session | `memory/recent.md`, `tasks/todo.md` | Session start |

## The Golden Rule

**Knowledge should live at the highest layer where it's universally true, and the lowest layer where it's specific enough to be useful.**

- "Plan before building" → L0 (all agents, all projects)
- "We use Jira for task tracking" → L1 (all of 7Ei)
- "I communicate in a direct, Swiss-German style" → L2 (one agent)
- "Use the T token object for colors" → L3 (one repo)
- "Currently blocked on API auth" → L4 (this session)
