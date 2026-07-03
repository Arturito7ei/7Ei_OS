# Runtime adapter — Claude Code / Cowork (Dispatch)

How the neutral onboarding path maps to a Claude session.

- **Identity loading**: `~/.claude/CLAUDE.md` imports `@~/Developer/7Ei_OS/protocols/principles.md` and `@~/Developer/7Ei_OS/agents/<instance>.md` (requires a local 7Ei_OS checkout, kept fresh with `git pull`). Project conventions come from each repo's layered `CLAUDE.md` — do not duplicate them in the agent file.
- **Token path**: `MC_AGENT_TOKEN` lives in the local shell env or macOS keychain — never in a committed file. Claude asks the human to place it; Claude does not handle the raw value in chat.
- **Checklist section A**: run the curls via shell with the env token, e.g. `curl -H "Authorization: Bearer $MC_AGENT_TOKEN" https://7ei-backend.fly.dev/api/agent/me`.
- **Memory habit**: Claude Code sessions ALSO write the session summary via the MC endpoint (not only local auto-memory) so other runtimes see it. Do it at session end per `protocols/session-continuity.md`.
- **Skills**: Claude Skills/plugins cover much of Stage 4 tooling (Jira MCP, Google MCPs). Inventory with the runtime's tool list; map gaps to `integrations/`.
- **Verification quirk**: `cd backend && npm test` for MC must run on the host Mac, not a Linux sandbox (darwin-arm64 node_modules).
