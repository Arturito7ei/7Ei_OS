# Runtime adapter — Cursor

- **Identity loading**: Cursor reads `.cursorrules` / `AGENTS.md`, not CLAUDE.md. In repos where Cursor operates, keep an `AGENTS.md` and have `CLAUDE.md` import it (`@AGENTS.md`) so both toolchains share one source. Agent identity: paste-import from `agents/<instance>.md` via the repo's Cursor rules, or use the one-step prompt-import in MC Cockpit.
- **MC access**: use the `7ei-mc` CLI (`7Ei-Mission_Control_App/cli/`, zero-dep Node) — `mc me`, `mc tasks`, `mc claim`, `mc result`, `mc heartbeat` — with `MC_AGENT_TOKEN` in env. The CLI covers checklist section A end to end.
- **Adapter option**: for autonomous polling, run the generic adapter with the `cursor` notes in `adapters/cursor/`.
- **Skills**: skill-library via repo clone; no bundled skills.
