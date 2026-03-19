# Naming Conventions

Consistent naming across the 7Ei ecosystem — agents, repos, branches, and entities.

## Agent Naming

### Pattern
```
{Name}7Ei{Runtime}
```

| Component | Description | Examples |
|-----------|-------------|---------|
| `{Name}` | Agent's given name or role | Arturito, Legal, Tech, Finance |
| `7Ei` | Organization marker (always present) | — |
| `{Runtime}` | Platform identifier | Claude, Claw, GPT |

### Active Agents
| Full Name | Name | Runtime | Role |
|-----------|------|---------|------|
| Arturito7EiClaude | Arturito | Claude Code | Master Orchestrator |
| Arturito7EiClaw | Arturito | OpenClaw | Operations, Browser + Telegram |

### Template
The primordial template is **Arturito7EiT** (the "T" stands for Template). All agents inherit from it.

## Repository Naming

### Pattern
- Org: `Arturito7ei` (GitHub organization)
- Repos: PascalCase or kebab-case, prefixed with `7Ei` where appropriate

### Current Repos
| Repo | Purpose |
|------|---------|
| `7Ei_OS` | Agent operating system (this repo) |
| `7ei-mission-control-v2` | Mission Control platform (Next.js) |
| `Open7Ei-MC` | Mission Control landing/UI (React + Vite) |
| `7EiBank` | Decentralised central bank for AI agents |
| `7EiAI-Website` | 7Ei website |
| `Arturito7ei` | Agent identity, memory, config (profile repo) |
| `skill-library` | Shared agent skills |

## Branch Naming

### Pattern
```
claude/<description>-<session-id>
```

Rules:
- Always prefixed with `claude/` for Claude Code sessions
- Description in kebab-case
- Session ID appended for traceability
- Never push to `main` directly — always branch and PR

### Examples
```
claude/resume-mission-control-B853g
claude/add-jira-skill-X7f2k
claude/fix-auth-flow-A3m9p
```

## Commit Messages

### Format
```
<scope>: <what changed and why>
```

### Scopes
| Scope | When |
|-------|------|
| `os` | Changes to 7Ei_OS |
| `mc` | Mission Control changes |
| `bank` | 7EiBank changes |
| `skill` | Skill library changes |
| `agent` | Agent identity/memory changes |
| `fix` | Bug fixes |
| `docs` | Documentation only |

### Examples
```
os: add coordination protocol for multi-agent task handoff
mc: implement agent squad panel with real-time status
bank: add whitepaper draft and legal structure
skill: add jira-openclaw skill for headless Jira management
fix: resolve token refresh loop in auth middleware
```

## File Naming

| Type | Convention | Example |
|------|-----------|---------|
| Protocol files | kebab-case `.md` | `session-continuity.md` |
| Agent identity | `AGENT.md` (uppercase) | `agents/arturito7eiclaude/AGENT.md` |
| Platform config | `CLAUDE.md` (uppercase) | `CLAUDE.md` |
| Skills | kebab-case directory | `jira-openclaw/` |
| Task handoffs | `TASK-NNN.yaml` | `TASK-001.yaml` |
| Memory files | kebab-case `.md` | `long-term.md`, `recent.md` |

## Project Naming

7Ei projects and products:
- **Open7Ei Mission Control** — the agent orchestration platform
- **7EiBank** — decentralised central bank for AI agents
- **7Ei_OS** — the agent operating system
- **7Ei** — the parent organization (7Ei AG, Swiss)
