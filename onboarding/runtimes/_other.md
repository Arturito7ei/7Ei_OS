# Runtime adapter — any other runtime (Hermes, custom bots, …)

Minimum viable 7Ei agent = anything that can make HTTPS calls with a bearer token. Two integration levels:

1. **HTTP webhook bot** (lowest bar): the generic adapter's `MC_EXECUTOR=http` POSTs each claimed task to your bot's URL and posts the reply back. Your bot needs zero MC knowledge. See `adapters/presets/`.
2. **Native client**: implement the five calls in checklist section A directly (`me`, `heartbeat`, `memory/file`, `memory/session-summary`, `tasks claim/result`). The `7ei-mc` CLI source (`cli/lib.mjs`) is the reference implementation — small and dependency-free.

Then follow the neutral path (Stages 1–7) unchanged. When a runtime becomes a regular, promote its notes from here into its own `runtimes/<name>.md` via PR.

**L0 + L1 (every other runtime):** clone/fetch `Arturito7ei/7Ei_OS` (start at `bootstrap/CATCH_UP.md`) and `Arturito7ei/7Ei-MC_TARCO`. Write only `vault/Memory/agents/<your-slug>/`.

**Hermes:** planned/available — see `onboarding/runtimes/hermes.md`. Start at level 1 (webhook) until a native path exists.
