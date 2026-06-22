# Paperclip Integration

How the TARCO Paperclip control plane syncs with 7Ei_OS and the Obsidian vault.

## Overview

| System | Role | Source of Truth For |
|--------|------|---------------------|
| **Paperclip** | Agent runtime, task orchestration, heartbeats | Live agent config, org chart, task state |
| **7Ei_OS** | Layer 0 operating system | Protocols, skills catalog, agent template DNA |
| **TARCO-MC_Vault** | Layer 1 shared memory | Human/agent-readable org knowledge, agent registry mirror |

## Company

- **Name:** TARCO
- **Paperclip ID:** `cf3b1159-c9f6-48e3-accd-d8a0b453043b`
- **Issue prefix:** TAR

## Active Agents (2026-06-22)

| Agent | Role | Adapter | Reports To | Vault Note |
|-------|------|---------|------------|------------|
| ArturitoGP | CEO | grok_local | — | `07-Agents/Agent — ArturitoGP.md` |
| CTO | CTO | grok_local | ArturitoGP | `07-Agents/Agent — CTO.md` |
| Arturito R2D2 | General / Orchestrator | grok_local | ArturitoGP | `07-Agents/Agent — Arturito R2D2.md` |

Vault index: `07-Agents/MOC-Agents.md`

## Sync Rules

### Paperclip → Vault (`07-Agents/`)
When agents are hired, updated, or removed in Paperclip:
1. Refresh agent notes in `vault/07-Agents/`
2. Update `MOC-Agents.md` table and org chart
3. Do **not** copy secrets (auth tokens, private keys) into vault notes

### 7Ei_OS → Vault (`Skill-Library/`)
When `skills/catalog.md` changes:
```bash
cd 7Ei_OS && python3 skills/sync_vault.py
```

### 7Ei_OS → Vault (`Protocols/`)
When L0 protocols change, update vault protocol summaries and link back to 7Ei_OS source files.

### Vault → 7Ei_OS
Org-facing knowledge (ADRs, company values) originates in vault. Promote to 7Ei_OS only when it becomes universal L0 truth.

## Agent Instructions

Paperclip managed instruction bundles live at:
```
~/.paperclip/instances/default/companies/{companyId}/agents/{agentId}/instructions/
```

Vault agent notes link to these paths; they are not duplicated in the vault.

## API Access

```bash
# List agents
GET /api/companies/{companyId}/agents

# Agent detail
GET /api/agents/{agentId}
```

Env vars injected at heartbeat: `PAPERCLIP_API_URL`, `PAPERCLIP_API_KEY`, `PAPERCLIP_COMPANY_ID`, `PAPERCLIP_AGENT_ID`.

## Related

- `integrations/obsidian.md` — vault structure and access
- `knowledge/sync.md` — cross-layer sync protocol
- `architecture/agent-hierarchy.md` — template → instance model
