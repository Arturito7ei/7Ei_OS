# Catch-up pack

> Mandatory first-read for any new or swapped agent, any runtime. Index only — open the linked files; do not copy them into your runtime.

**Last updated:** 2026-10-21

## Layers

| Layer | Meaning | Where |
|-------|---------|-------|
| L0 | How agents operate | this repo (`Arturito7ei/7Ei_OS`) |
| L1 | What 7Ei knows | Obsidian vault git `Arturito7ei/7Ei-MC_TARCO` (`vault/`) |
| L2 | Who you are | runtime-private identity (Buzz core, `AGENT.md`, …) — not this repo |

Write L1 memory only in `vault/Memory/agents/<your-slug>/`. Read anywhere. Propose L0 changes via PR (`CONTRIBUTING.md`).

## Read order (do this)

1. **How** — `ARCHITECTURE.md` · `protocols/memory.md` · `protocols/session-continuity.md` · `protocols/governance.md` · `protocols/workflow.md` · `protocols/knowledge-boundaries.md`
2. **Who** — vault `vault/Memory/agents/README.md` + `vault/07-Agents/MOC-Agents.md` (L1 seats). This repo `agents/README.md` (instance profiles; may lag).
3. **What's live** — `memory/CLAUDE.md` (hot cache, 2026-10-21). Then vault `Company/Goals-Now.md` and `Memory/project.md`. Those three files are the board. Ignore older sprint plans when they disagree.
4. **Runtimes** — runtime table in `README.md`. Do not treat a runtime as Active unless that table says so.
5. **Blueprints** — `blueprints/README.md` (how we orchestrate agents).
6. **Runtime adapter** — `onboarding/runtimes/<your-runtime>.md`. If none exists, `onboarding/runtimes/_other.md`.

## L1 vault (facts)

- Git: `Arturito7ei/7Ei-MC_TARCO`. Start: `vault/00-Index/MOC-home.md`. Activity: `vault/07-Agents/Activity.md`.
- Write namespaces (Buzz fleet, 2026-08-14): `7man` · `7rd` · `7ops` · `7dev` · `7fin` · `7mkt`. No `7lex` folder yet.
- Legacy **read-only** (no new writes): `openclaw` and the other pre-Buzz slugs listed in that README.
- Coordination bus: Mission Control (`https://7ei-backend.fly.dev`) — `protocols/coordination.md`. The product is **paused**. Do not start a feature sprint from this bus.
- Closed until further notice (owner, 2026-10-21): 7EiBank, 7PolyBet, Hypnomaster.
- Killed the same day: radar trials `hermes-official-plugins` and `pensieve`. Do not install them.

## After this file

- Brand-new instance: `onboarding/README.md`, then pass `onboarding/checklist.md`.
- Skills inventory: `skills/catalog.md` (before taking a task).
- Hard call or 777 Gate: `protocols/silver-board.md` (product lives in `Arturito7ei/silver-board`, not in this OS).
