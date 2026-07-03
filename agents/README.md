# Agent Instances

> Profiles of all active agent instances operating under 7Ei.

## What Is an Agent Instance?

An agent instance is a specific deployment of the 7Ei agent template (`architecture/agent-template.md`) running on a particular runtime. The same "Arturito" identity can have multiple instances across different runtimes (Claude Code, Dispatch, Open Claw) — each with different capabilities but sharing the same core identity and protocols.

## Active Instances

| Instance | Runtime | Primary Role | Status |
|----------|---------|-------------|--------|
| [[arturito-dispatch]] | Claude Dispatch (Cowork) | Sprint planning, tool orchestration, remote ops | Active |
| [[arturito-claude-code]] | Claude Code | Code execution, work order implementation | Active |
| [[arturito-openclaw]] | Open Claw + Telegram | Operations, browser automation, Jira | Active |

## Instance vs. Identity

- **Identity** (Layer 2) = who the agent IS (name, role, personality, values)
- **Instance** = a specific deployment of that identity on a runtime
- All instances of the same agent share the same identity file
- Each instance has its own capabilities, permissions, and integrations

## Creating a New Instance

1. Choose a runtime (Claude Code, Dispatch, Open Claw, Cursor, etc.)
2. Create an instance profile in this folder
3. Reference the identity from `identity/`
4. Define instance-specific capabilities and permissions
5. Follow `onboarding/README.md` for first-time setup (verification gate: `onboarding/checklist.md`)

## Paperclip Agents (TARCO)

TARCO runs on [Paperclip](https://paperclip.ing) for task orchestration and heartbeats. The vault mirror lives in `TARCO-MC_Vault/07-Agents/`.

| Agent | Role | Runtime | Vault Note |
|-------|------|---------|------------|
| ArturitoGP | CEO | grok_local | `07-Agents/Agent — ArturitoGP.md` |
| CTO | CTO | grok_local | `07-Agents/Agent — CTO.md` |
| Arturito R2D2 | Orchestrator | grok_local | `07-Agents/Agent — Arturito R2D2.md` |

See `integrations/paperclip.md` for sync rules between Paperclip, 7Ei_OS, and the vault.
