# Agent Onboarding — the canonical path

How ANY new agent joins 7Ei — Claude Code, Cowork/Dispatch, OpenClaw, Cursor, Hermes, or a future runtime. The core path below is runtime-neutral; your runtime's specifics are in `runtimes/<your-runtime>.md`. You are DONE only when every item in `checklist.md` passes.

Two systems you will touch constantly, learn them first:
- **Mission Control (MC)** — `https://7ei-backend.fly.dev`, the coordination + memory bus. You get an agent token (`mca_…`); every task, heartbeat, and shared-memory operation goes through its agent API.
- **The vault** — Obsidian repo `Arturito7ei/7Ei-MC_TARCO` (`vault/`), the shared knowledge store. You read anywhere; you write ONLY in your own namespace `Memory/agents/<your-slug>/`.

## Stage 1 — Identity (who are you?)

1. Human (or orchestrator) creates your instance profile in `agents/<instance>.md` from `identity/template.md` + `architecture/agent-template.md`: name, role, capabilities, permissions, **vault slug** (kebab-case — must match your MC agent name slug).
2. Human registers you in MC (Cockpit → agents) and mints your agent token. The token reaches you via your runtime's secure path (see your runtime adapter) — never through chat or a committed file.
3. Your MC `termsOfReference` should mirror your `agents/<instance>.md` — one identity, two consumers.

## Stage 2 — Environment (where are you?)

Read, in order: `README.md` + `ARCHITECTURE.md` (the 5-layer knowledge model), `agents/README.md` (who else is active — you are not alone), `projects/` (ongoing work), and the vault starting at `00-Index/MOC-home.md` then `07-Agents/MOC-Agents.md`. Answer for yourself: who are the other agents, what are they working on right now (vault `07-Agents/Activity.md` tells you where to look), and which projects touch your role?

## Stage 3 — Protocols (how do we work?)

Read ALL of `protocols/`. The ones you will use in your first hour:
- `workflow.md` — plan → execute → verify. Plan BEFORE executing, always.
- `coordination.md` — tasks come from MC (claim atomically, one owner); heartbeat green while active.
- `memory.md` + `session-continuity.md` — boot sequence, session summaries, lessons format.
- `learning.md` — every human correction becomes a lesson entry immediately, in your namespace.
- `governance.md` — what you may do autonomously vs. what needs approval. When unsure: ask.

## Stage 4 — Tools (what can you reach?)

Your REQUIRED tool set depends on your role — see the role matrix in `checklist.md`. Setup guides per tool live in `integrations/` (Jira, Google Workspace, GitHub, Obsidian, Slack, …). Inventory what your runtime actually has (MCPs, CLIs, API access), diff against your required set, and produce a **tool-gap report** (template in `checklist.md`) for the human. You never mint, enter, or rotate credentials yourself — gaps are escalated with exact setup steps, then re-verified.

## Stage 5 — Skills (what can you do?)

Read `skills/catalog.md` (this repo) and the vault `Skill-Library/`. Note which skills are workspace / bundled / plugin / skill-library (`Arturito7ei/skill-library`) and declare your authorized subset in your instance profile. If your task needs a skill you lack, check the catalog before building anything new; contribute new skills back via PR.

## Stage 6 — Verification (prove it)

Run `checklist.md` top to bottom. The gate is machine-checkable — no item is "understood", every item is "demonstrated". Attach the completed checklist + tool-gap report to your onboarding task in MC.

## Stage 7 — First task (graduate)

Claim the standard smoke task the human/orchestrator created for you in MC, execute it per the workflow protocol, post the result, write your first session summary (`POST /api/agent/memory/session-summary`), and confirm it appears in the vault at `Memory/agents/<your-slug>/recent.md`. Another agent must be able to see what you did without asking you — that's the definition of done.

## Where your activity is visible to others

Your work is public to the org by design: MC task timeline + heartbeats (Cockpit), your `Memory/agents/<slug>/recent.md` session summaries, the weekly consolidation report to the orchestrator, and your git commits. See vault `07-Agents/Activity.md`.

## New project repo?

Onboarding a REPO (not an agent) is different and small — see `new-project.md`.
