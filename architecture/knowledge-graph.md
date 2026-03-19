# Knowledge Graph

How 7Ei agents build, maintain, and query organizational knowledge through Obsidian vaults and structured research.

## Knowledge Architecture

7Ei knowledge lives in two complementary systems:

```
Obsidian Vaults (rich, linked, human-friendly)
    ↕ sync
Git Repos (versioned, agent-friendly, source of truth)
```

### Obsidian Vaults

| Vault | Purpose | Access |
|-------|---------|--------|
| **Open7EiMc** | Mission Control platform data, planning, architecture | Arturito7EiClaude |
| **Open7Ei_ObsidianVault** | Shared collaboration vault | All agents |

### Git Repos (Knowledge Layer)

| Repo | Knowledge Type |
|------|---------------|
| `7Ei_OS` | Layer 0 — universal protocols (this repo) |
| `Arturito7ei` | Layer 2 — agent identity, memory, lessons |
| Each project repo | Layer 3 — project-specific knowledge |

## Knowledge Flow

```
Research / Discovery
    ↓
Agent records in memory/recent.md (Tier 2)
    ↓
Stable knowledge? → Promote to memory/long-term.md (Tier 1)
    ↓
Universal pattern? → Propose to 7Ei_OS (Layer 0) via PR
    ↓
Permanent reference? → Add to Obsidian vault with backlinks
```

## Obsidian Integration

### Vault Structure

Obsidian vaults follow a consistent structure:

```
vault/
├── 00-Index/           # MOCs (Maps of Content) and navigation
├── 01-Projects/        # Active project notes
├── 02-Architecture/    # Technical architecture decisions
├── 03-Research/        # Research notes and findings
├── 04-Meetings/        # Meeting notes and decisions
├── 05-Templates/       # Note templates
└── 06-Archive/         # Completed/deprecated content
```

### Naming Conventions
- Notes: `YYYY-MM-DD-descriptive-title.md`
- MOCs: `MOC-domain-name.md`
- ADRs: `ADR-NNN-decision-title.md`
- Templates: `Template-type.md`

### Linking Strategy
- Use `[[wikilinks]]` for internal connections
- Tag with `#domain/topic` for discoverability
- Every note links back to its MOC
- Orphan notes (no backlinks) should be reviewed weekly

## Research Pipeline

When an agent needs to research a topic:

1. **Search** — web search, documentation, existing vault notes
2. **Capture** — raw findings to `memory/recent.md` or a scratch note
3. **Synthesize** — distill into structured knowledge
4. **Store** — place at the correct knowledge layer:
   - Session-specific → `memory/recent.md`
   - Stable finding → `memory/long-term.md`
   - Project-specific → project docs or Obsidian
   - Universal → propose to `7Ei_OS`
5. **Link** — connect to related knowledge in Obsidian via backlinks

## MCP Integration

Agents can access Obsidian vaults via MCP (Model Context Protocol) servers:

- Read and search vault notes
- Create and update notes
- Query by tags, backlinks, or full-text search
- Sync changes back to Git

Configure in the agent's MCP settings. The vault path must be accessible from the agent's runtime environment.

## Knowledge Quality Rules

1. **No duplication** — if knowledge exists somewhere, link to it, don't copy it
2. **Single source of truth** — every fact has one canonical location
3. **Layer-appropriate** — use the boundary test (`protocols/governance.md`) to place knowledge correctly
4. **Agent-consumable** — write so that any LLM can parse and act on the information
5. **Linked** — isolated knowledge is lost knowledge; always connect to related context
6. **Dated** — include creation/update dates for staleness detection
