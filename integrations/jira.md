# Jira Integration

How 7Ei agents interact with Jira for project and sprint management.

## Instance

- **URL:** `https://7ei.atlassian.net`
- **Primary Project:** O7MC (Open7Ei Mission Control)
- **Auth:** API token (stored in `.env`, never committed)

## Access Methods

### Headless Agents (Recommended)
Use the `jira-openclaw` skill from the shared skill library. This uses API token auth via `curl` — works on Claude Code, OpenClaw, Telegram bots, CI/CD pipelines, or any runtime that can execute bash.

```bash
source skills/jira-openclaw/scripts/jira.sh
jira_load_env
jira_whoami  # verify connection
```

See `skill-library/jira-openclaw/SKILL.md` for complete documentation.

### Browser-Based Agents
Agents with browser access (e.g., Arturito7EiClaw) can use the Jira web UI directly.

### Atlassian MCP
The official Atlassian MCP works for agents with OAuth browser flow capability. Use alongside the headless skill when Confluence access is also needed.

## Environment Setup

```bash
# .env (never commit this file)
JIRA_BASE_URL=https://7ei.atlassian.net
JIRA_EMAIL=arturito@7ei.ai
JIRA_API_TOKEN=<your-token>
JIRA_PROJECT=O7MC
```

Create API tokens at: `https://id.atlassian.com/manage-profile/security/api-tokens`

## Project Spaces

| Key | Project | Description |
|-----|---------|-------------|
| O7MC | Open7Ei Mission Control | Platform development, sprints, backlog |

## Common Operations

### Creating Tasks
```bash
jira_create_task "Implement agent status panel" "Add real-time status for all agents" "High"
```

### Querying
```bash
jira_search "project = O7MC AND status != Done ORDER BY priority"
jira_report "project = O7MC AND priority in (Highest, High) AND status != Done"
```

### Status Transitions
```bash
jira_start O7MC-1    # → In Progress
jira_done O7MC-1     # → Done
```

## Issue Conventions

### Types
- **Epic** — large feature or initiative (multiple sprints)
- **Task** — actionable work item (fits in a sprint)
- **Sub-task** — breakdown of a task
- **Bug** — defect requiring fix

### Priority Scale
| Priority | Use For |
|----------|---------|
| Highest | Launch blockers, production incidents |
| High | Sprint commitments, critical path |
| Medium | Important but not blocking |
| Low | Nice-to-have, backlog |
| Lowest | Someday/maybe |

### Summaries
- Be specific and actionable: "Implement JWT token refresh" not "Fix auth"
- Start with a verb: "Add", "Fix", "Update", "Remove", "Investigate"
- Include the component or area if relevant: "API: Add rate limiting middleware"

## Red Flags

- **Hardcoded transition IDs** — use `jira_move_to` (IDs vary by workflow)
- **Orphan tasks** — use parent tasks to group related work
- **Priority inflation** — reserve Highest for production issues only
- **Stale boards** — transition status as work progresses
- **Committed credentials** — `.env` must be in `.gitignore`
