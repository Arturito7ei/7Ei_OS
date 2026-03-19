# Agent Hierarchy

How the Arturito7EiT template becomes concrete agent instances with specialized roles.

## The 3 Levels

```
TEMPLATE (Arturito7EiT)
│
│   Defines: protocols, principles, memory architecture, governance
│   Lives in: 7Ei_OS
│   Changes: Rarely. Human approval required.
│
├── INSTANCE (Arturito7EiClaude, Arturito7EiClaw, ...)
│   │
│   │   Defines: identity, personality, runtime, skill subset
│   │   Lives in: agents/{instance}/AGENT.md
│   │   Changes: Per session or on role changes
│   │
│   └── SPECIALIZATION (per project role)
│       │
│       │   Defines: project context, tech stack, team role
│       │   Lives in: each repo's CLAUDE.md + .claude/rules/
│       │   Changes: Per sprint or architectural change
```

## Active Instances

### Arturito7EiClaude
- **Runtime:** Claude Code
- **Role:** Master Orchestrator, Chief of Staff
- **Capabilities:** Code generation, architecture, planning, multi-repo orchestration, subagent delegation
- **Projects:** All 7Ei repos (Open7Ei-MC, 7EiBank, 7Ei_OS, skill-library, Arturito7ei, 7EiAI-Website)
- **Coordination:** Creates task handoffs, reviews PRs, manages priorities

### Arturito7EiClaw
- **Runtime:** OpenClaw + Telegram
- **Role:** Operations, external tool access
- **Capabilities:** Browser automation, Telegram messaging, Jira management, GitHub actions via API
- **Projects:** skill-library (contributor), coordination tasks
- **Coordination:** Picks up task handoffs, reports via Telegram, manages Jira boards
- **Contributed:** `jira-openclaw` skill to the shared skill library

## Naming Convention

```
{Name}7Ei{Runtime}
│       │    │
│       │    └── Runtime: Claude, Claw, etc.
│       └── Organization marker (always "7Ei")
└── Agent's given name or role descriptor
```

Examples:
| Agent Name | Breakdown | Description |
|-----------|-----------|-------------|
| Arturito7EiClaude | Arturito + 7Ei + Claude | Primary orchestrator on Claude Code |
| Arturito7EiClaw | Arturito + 7Ei + Claw | Primary orchestrator on OpenClaw |
| Legal7EiClaude | Legal + 7Ei + Claude | Legal specialist agent |
| Tech7EiClaw | Tech + 7Ei + Claw | Technical lead on OpenClaw |
| Finance7EiClaude | Finance + 7Ei + Claude | Financial operations agent |

## Instance vs Template Knowledge

| Question | If YES → | If NO → |
|----------|----------|---------|
| Does every agent need this? | Template (7Ei_OS) | Instance (AGENT.md) |
| Is this about how I work? | Template | Instance |
| Is this about who I am? | Instance | Template or Project |
| Is this about what I'm working on? | Project (CLAUDE.md) | Template or Instance |

## Spawning New Instances

See `protocols/spawning.md` for the complete checklist. Key decisions when creating a new instance:

1. **Runtime** — Which platform will this agent run on?
2. **Role** — What is this agent's primary purpose?
3. **Skill subset** — Which skills from the library does it need?
4. **Projects** — Which repos does it have access to?
5. **Coordination** — How does it communicate with other agents?

## Orchestrator Responsibilities

Arturito7EiClaude (or whichever agent holds the orchestrator role):

- Routes tasks to the best-equipped agent
- Reviews cross-agent PRs and knowledge promotions
- Resolves conflicts between agents
- Maintains the OS (this repo) and proposes updates
- Monitors agent heartbeats and flags inactive agents
- Approves Tier 2 governance actions
