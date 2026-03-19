# Governance Protocol

## Approval Tiers

### Auto-Approved (No Confirmation)
- Local file reads and edits
- Test execution
- Research queries (web search, file exploration)
- Internal agent communication
- Memory updates (within own tier)

### Requires Orchestrator Approval
- External API calls with side effects
- Budget reallocation between projects
- Spawning new agent instances
- Cross-project resource sharing
- Promoting knowledge to Layer 0 or Layer 1

### Requires Human Approval
- Destructive operations (delete, force-push, reset)
- External communications (email, social media, PR comments)
- Financial transactions
- Governance rule changes
- Publishing or deploying to production
- Changes to 7Ei_OS protocols

## Audit Trail

All significant actions are logged across:
- `memory/recent.md` — session-level decisions
- `tasks/lessons.md` — corrections and pattern changes
- Git history — complete change history
- Obsidian vault — permanent knowledge base

## Budget Controls

- Each project has a defined resource budget
- Agents track spend against budget
- 80% threshold → warning to orchestrator
- 100% threshold → hard stop, requires human override
- Monthly reset with configurable rollover
