# Obsidian Integration

How 7Ei agents use Obsidian vaults for persistent, linked knowledge management.

## Canonical Vault

| Vault | Path | Purpose | Primary Users |
|-------|------|---------|---------------|
| **TARCO-MC_Vault** | `~/Library/Mobile Documents/com~apple~CloudDocs/7Ei-MC_TARCO_Vault/TARCO-MC_Vault` | L1 org memory + MC planning, architecture, skills, Paperclip agent registry | All TARCO agents |

> Legacy names `Open7EiMc` and `Open7Ei_ObsidianVault` refer to earlier vault iterations. **TARCO-MC_Vault** is the current canonical vault (see vault `ADR-002-obsidian-shared-memory-vault`).

## Vault Structure

```
TARCO-MC_Vault/
├── 00-Index/           # Maps of Content (MOCs), navigation
├── 01-Projects/        # Active project notes and plans
├── 02-Architecture/    # ADRs, system design, tech decisions
├── 03-Research/        # Research notes, competitive analysis
├── 04-Meetings/        # Meeting notes, decisions, action items
├── 05-Templates/       # Reusable note templates
├── 06-Archive/         # Completed or deprecated content
├── 07-Agents/          # Paperclip agent registry (runtime mirror)
├── Company/            # L1 org identity, values, legacy instances
├── Memory/             # 4-tier operational memory files
├── Protocols/          # Local summaries of 7Ei_OS protocols
└── Skill-Library/      # Canonical skill/tool registry (derived from 7Ei_OS catalog)
```

## Tri-Sync Model (7Ei_OS ↔ Vault ↔ Paperclip)

| Layer | Source of Truth | Sync Target | Mechanism |
|-------|----------------|-------------|-----------|
| L0 OS protocols | `7Ei_OS/` (this repo) | `vault/Protocols/` summaries | Manual on protocol change; link back to 7Ei_OS |
| L0 skills catalog | `7Ei_OS/skills/catalog.md` | `vault/Skill-Library/` | `python3 skills/sync_vault.py` |
| L1 agents (Paperclip) | Paperclip API | `vault/07-Agents/` | Manual or scripted refresh on agent change |
| L1 org knowledge | `vault/Company/` | — | Vault is SoT for org-facing knowledge |

See `integrations/paperclip.md` for Paperclip-specific sync rules.

## Access Methods

### obsidian-cli (Yakitrak)
Direct filesystem access — no Obsidian app required:
```bash
obsidian-cli list
obsidian-cli print "07-Agents/MOC-Agents"
obsidian-cli search "paperclip"
```

### MCP (Model Context Protocol)
Agents with MCP access can read, search, and write vault notes directly.

### iCloud Sync
Cross-device sync for humans. Agent writes go directly to filesystem.

### Git Backup
Vault backed up to Git (`Arturito7ei/7Ei-MC_TARCO`). Git is the conflict-resolution source of truth.

## Note Conventions

### Naming
- Standard notes: `YYYY-MM-DD-descriptive-title.md`
- Maps of Content: `MOC-domain-name.md`
- Architecture Decision Records: `ADR-NNN-decision-title.md`
- Templates: `Template-type.md`
- Agent notes: `Agent — {Name}.md`

### Linking
- Use `[[wikilinks]]` for internal connections
- Tag with `#domain/topic` hierarchical tags
- Every note should link back to its relevant MOC

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
