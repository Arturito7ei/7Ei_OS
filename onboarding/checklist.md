# Onboarding Verification Gate

Every item is a demonstrable action, not a claim. Run top to bottom; paste the completed checklist + tool-gap report into your MC onboarding task. An agent that cannot complete Section A is NOT onboarded, whatever else it knows.

## A — Mission Control (mandatory for every agent)

| # | Check | How | Pass |
|---|-------|-----|------|
| A1 | Authenticate | `GET /api/agent/me` returns your identity | ☐ |
| A2 | Heartbeat | `POST /api/agent/heartbeat` → green visible in Cockpit | ☐ |
| A3 | Read shared memory | `GET /api/agent/memory/file?path=vault/Memory/long-term.md` returns content | ☐ |
| A4 | Write own namespace | `POST /api/agent/memory/session-summary` → commit lands in `Memory/agents/<slug>/recent.md` | ☐ |
| A5 | Task lifecycle | Claim the smoke task (`POST /tasks/:id/claim`), complete it (`/result`), status reaches done | ☐ |
| A6 | Know your gates | State which of your capabilities are permission-gated and which actions trigger approval requests (from your instance profile + `governance.md`) | ☐ |

## B — Knowledge (mandatory)

| # | Check | How | Pass |
|---|-------|-----|------|
| B1 | Layer test | Answer: "If I learn something new, which layer does it belong to and where do I store it?" (per `ARCHITECTURE.md`) | ☐ |
| B2 | Skill lookup | Answer: "What skill do I use for X?" pointing to the correct `skills/catalog.md` entry | ☐ |
| B3 | Awareness | Name the other active agents and one thing each is currently working on (from MC + vault Activity page) | ☐ |
| B4 | Protocols ack | Confirm you read all `protocols/` and state the plan→execute→verify rule in one sentence | ☐ |

## C — Tools (role-dependent)

Required set by role — derive yours, then inventory what your runtime can actually reach:

| Role archetype | Required | Recommended |
|---|---|---|
| Builder (code) | GitHub, MC agent API, vault (via MC) | Jira, Google Drive |
| Orchestrator | MC agent API, Jira/Atlassian, vault, Telegram (human ping) | Google Calendar, Gmail |
| Operator (browser/comms) | MC agent API, Telegram, browser automation | WhatsApp, TTS, Google Workspace |
| Analyst/CEO-advisor | MC agent API, vault, Google Drive/Gmail/Calendar | Jira, TTS |

Setup guides: `integrations/<tool>.md`. If a needed integration has no guide, flag that too.

### Tool-gap report (paste into your onboarding task)

```markdown
## Tool-gap report — <agent> on <runtime>, <date>
| Tool | Required? | Present? | Evidence (command/endpoint tried) | Setup needed (integrations/ link) |
|------|-----------|----------|-----------------------------------|-----------------------------------|
Human actions needed: <numbered list, exact console steps, no credentials in this file>
```

## D — Sign-off

- ☐ Instance profile exists in `agents/` and matches MC TOR
- ☐ Checklist + gap report attached to the MC onboarding task
- ☐ First session summary visible in vault
- ☐ Human or orchestrator marked the onboarding task done

Re-run Section A after any credential rotation or runtime move (e.g. laptop → Mac mini).
