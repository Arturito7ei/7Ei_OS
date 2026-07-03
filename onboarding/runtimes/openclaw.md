# Runtime adapter — OpenClaw (and any adapter-based runtime)

The adapter (`7Ei-Mission_Control_App/adapters/openclaw/mc_adapter.py`, stdlib-only Python) IS your MC client: it polls, claims, executes (shell | llm | http), heartbeats, and pulls scoped secrets at boot.

- **Install**: `adapters/mac-mini/setup.sh --preset <preset> --yes` with `MC_AGENT_TOKEN` — writes `~/.openclaw/mc-adapter/mc.env` (chmod 600, NO LLM key on disk; `MC_LLM_API_KEY` comes from the MC secret store at boot) and loads the launchd keep-alive.
- **Checklist section A**: A1/A2/A5 are exercised by `python3 mc_adapter.py --once` against a smoke task; watch `~/.openclaw/mc-adapter/adapter.log`. A3/A4 need the org's vault connector configured (`GITHUB_VAULT_TOKEN` in Cockpit → Secrets) — if boot logs show `loaded N scoped secret(s)` but memory calls 400 with "vault not connected", that's a tool gap to report.
- **Telegram**: optional completion pings via `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID` in `mc.env`.
- **Skills** by type: workspace (`7Ei_OS/skills/<name>/`, symlinked to `~/.openclaw/workspace/skills/`), bundled (OpenClaw install path), plugin (`~/.openclaw/plugin-skills/`), skill-library (clone `Arturito7ei/skill-library`). Verify vault sync: `python3 skills/sync_vault.py --dry-run`.
- **Known quirk**: NVIDIA NIM minimax requires `max_tokens` in requests (adapter handles it — don't remove).
- **Moving hosts** (laptop → Mac mini): rotate the agent token first (invalidates the old host), run setup on the new host, `launchctl unload` on the old one, re-run checklist section A.
