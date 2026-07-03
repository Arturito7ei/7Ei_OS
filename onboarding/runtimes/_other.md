# Runtime adapter — any other runtime (Hermes, custom bots, …)

Minimum viable 7Ei agent = anything that can make HTTPS calls with a bearer token. Two integration levels:

1. **HTTP webhook bot** (lowest bar): the generic adapter's `MC_EXECUTOR=http` POSTs each claimed task to your bot's URL and posts the reply back. Your bot needs zero MC knowledge. See `adapters/presets/`.
2. **Native client**: implement the five calls in checklist section A directly (`me`, `heartbeat`, `memory/file`, `memory/session-summary`, `tasks claim/result`). The `7ei-mc` CLI source (`cli/lib.mjs`) is the reference implementation — small and dependency-free.

Then follow the neutral path (Stages 1–7) unchanged. When a runtime becomes a regular, promote its notes from here into its own `runtimes/<name>.md` via PR.

**Hermes**: specifics unknown at time of writing — start at level 1 (webhook) and document what you learn here.
