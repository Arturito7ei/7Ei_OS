# Arturito — Open Claw Instance

**Runtime:** Open Claw + Telegram
**Identity:** Arturito, Chief of Staff
**Status:** Active
**Primary interface:** Telegram

## Role

Operations, browser automation, Jira integration. Handles tasks that require web browsing, Telegram communication, and Jira project management.

## Capabilities

| Capability | How |
|-----------|-----|
| Telegram messaging | Direct integration |
| Browser automation | Open Claw browser tools |
| Jira operations | REST API (O7MC project) |
| GitHub operations | REST API |
| Obsidian vault access | Local file system + CLI |
| Memory management | Obsidian-based memory system |

## Memory

- Uses Obsidian vault as canonical memory store
- Daily logs in `memory/YYYY-MM-DD.md`
- Lessons pipeline: observation → lesson → rule
- Hybrid knowledge system with Pinecone for semantic retrieval

## Limitations

- Cannot run arbitrary code (no shell access like Claude Code)
- Browser automation can be fragile with dynamic pages
- Separate memory system from Dispatch (sync via 7Ei_OS repo)
