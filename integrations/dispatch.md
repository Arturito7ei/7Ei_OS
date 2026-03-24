# Dispatch (Claude Cowork)

**Type:** AI orchestration interface
**Access:** Phone app (iOS/Android) + desktop
**Role:** Primary interface for Arturito to manage all 7Ei operations

## What Dispatch Does

- Sprint planning and execution management
- GitHub operations (PRs, issues, merges) via MCP
- Google Drive, Gmail, Calendar, Slack, Notion access
- Code session management (start, monitor, relay results)
- File creation and document generation

## Connected Integrations

| Integration | Status | Auth |
|-------------|--------|------|
| GitHub | ✅ Connected | OAuth |
| Google Drive | ✅ Connected | OAuth |
| Gmail | ✅ Connected | OAuth |
| Google Calendar | ✅ Connected | OAuth |
| Slack | ✅ Connected | OAuth |
| Notion | ✅ Connected | OAuth |
| Cloudflare | ✅ Connected | API Token |
| Vercel | ✅ Connected | API Token |
| Figma | ✅ Connected | OAuth |
| Hugging Face | ✅ Connected | API Token |

## Memory Sync

Dispatch reads from `7Ei_OS/memory/CLAUDE.md` at session start.
Lessons learned during sessions are written to `7Ei_OS/memory/lessons.md`.
Sprint plans are stored in `7Ei_OS/projects/{project}/sprints/`.

## Session Bootstrap Prompt

For new Dispatch sessions:
```
Read my 7Ei_OS memory at Documents/.claude/CLAUDE.md and the memory/ folder.
```
