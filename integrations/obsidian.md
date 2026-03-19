# Obsidian Integration

How 7Ei agents use Obsidian vaults for persistent, linked knowledge management.

## Vaults

| Vault | Purpose | Primary Users |
|-------|---------|---------------|
| **Open7EiMc** | Mission Control platform planning, architecture, project data | Arturito7EiClaude |
| **Open7Ei_ObsidianVault** | Shared collaboration vault — cross-agent knowledge | All agents |

## Vault Structure

```
vault/
├── 00-Index/           # Maps of Content (MOCs), navigation
├── 01-Projects/        # Active project notes and plans
├── 02-Architecture/    # ADRs, system design, tech decisions
├── 03-Research/        # Research notes, competitive analysis
├── 04-Meetings/        # Meeting notes, decisions, action items
├── 05-Templates/       # Reusable note templates
└── 06-Archive/         # Completed or deprecated content
```

## Access Methods

### MCP (Model Context Protocol)
Agents with MCP access can read, search, and write vault notes directly:
- Full-text search across all notes
- Query by tags or backlinks
- Create and update notes programmatically
- Sync changes automatically

### Obsidian Sync
Vaults sync between devices and environments in real-time via Obsidian Sync. This is the primary sync mechanism for human users.

### Git Backup
Vaults are backed up to Git for version control and agent access when MCP is unavailable. Git is the source of truth for conflict resolution.

## Note Conventions

### Naming
- Standard notes: `YYYY-MM-DD-descriptive-title.md`
- Maps of Content: `MOC-domain-name.md`
- Architecture Decision Records: `ADR-NNN-decision-title.md`
- Templates: `Template-type.md`

### Linking
- Use `[[wikilinks]]` for internal connections
- Tag with `#domain/topic` hierarchical tags
- Every note should link back to its relevant MOC
- Review orphan notes (no backlinks) weekly

### Frontmatter
```yaml
---
title: Note Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [domain/topic, project/name]
status: active | draft | archived
---
```

## Agent Usage Rules

1. **Read before writing** — check if a note already exists before creating a new one
2. **Link, don't duplicate** — reference existing knowledge rather than copying it
3. **Respect layers** — vault notes are Layer 1 (org) or Layer 3 (project) knowledge, not session state
4. **Date everything** — include creation and update dates for staleness detection
5. **Archive, don't delete** — move to `06-Archive/` instead of deleting

## Relationship to Memory Protocol

```
Obsidian Vault                  Agent Memory Files
──────────────                  ──────────────────
Permanent reference knowledge   Rolling/tiered memory
Human-friendly (rich, linked)   Agent-friendly (flat, fast)
Updated manually or via MCP     Updated every session
Source of architectural truth   Source of operational truth
```

Use Obsidian for knowledge you want to persist permanently and link richly. Use memory files for operational context that drives day-to-day work.
