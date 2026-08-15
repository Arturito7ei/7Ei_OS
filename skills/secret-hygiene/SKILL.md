---
name: secret-hygiene
description: Retrieve and reference secrets by store item name only. Use when any task needs API tokens, keys, or credentials. Never print, commit, or paste secret values into chat, logs, or repos.
---

# Secret Hygiene

Prevent secret leakage across agents, chat, logs, and git. Reference secrets by **name**; never surface values.

**Cluster:** Operations  
**Owner:** 7OPS (author: 7RD)  
**Pairs with:** bundled `1password` skill (`op` CLI), `7Ei_OS/security/secrets-management.md`  
**Inspired by:** trailofbits `plugins/insecure-defaults` (CC-BY-SA-4.0 — patterns only, rewritten for 7Ei)  
**Sovereignty:** Local / BYOK — no new SaaS; operator controls 1Password vault and env files.

## When to Use

- Any task needs an API key, token, password, or credential
- Configuring BYOK (`gh`, LLM providers, Buzz relay, n8n, CI secrets)
- Reviewing code/config for insecure defaults (fallback secrets, hardcoded keys)
- Before committing, posting to Buzz, or logging command output
- After a suspected leak — coordinate rotation (human-only)

## Hard Rules (non-negotiable)

1. **Never paste secret values** into Buzz messages, PR descriptions, commit messages, issues, or chat of any kind.
2. **Never commit secrets** — not even private repos. No `.env` with real values in git.
3. **Never log secret values** — redact before writing logs, `.learnings/`, WORK_LOGS, or error reports.
4. **Never pass secrets in URLs** — query params are logged everywhere.
5. **Log only item names** — e.g. `op item "GitHub PAT — Arturito7ei"` or `~/.openclaw/secrets/mc.env` — never the value.
6. **Rotation is human-only** — escalate to 7OPS / operator; agents do not rotate production keys.
7. **Fail closed** — if a secret is missing, stop and ask; do not invent fallbacks (see §Insecure Defaults).

Canonical policy: `7Ei_OS/security/secrets-management.md`.

## Allowed Secret Stores

| Store | Path / access | Agent may |
|---|---|---|
| **1Password** | `op` CLI — item title in vault | Read via `op run` / `op inject` inside tmux (see bundled `1password` skill) |
| **OpenClaw scoped env** | `~/.openclaw/secrets/*.env` (chmod 600) | Source in shell; never cat into chat |
| **MC adapter env** | `~/.openclaw/mc-adapter/mc.env` (chmod 600) | Read path only; LLM keys pulled at boot from MC secret store |
| **Fly.io / GitHub repo secrets** | CI/CD and backend runtime | Agents call services that hold secrets — never read raw values |
| **Buzz harness env** | `BUZZ_PRIVATE_KEY`, `BUZZ_AUTH_TAG` set by harness | Use via CLI; never echo or write to RESEARCH |

**Forbidden:** pasting into `core` memory, skill files, vault notes, screenshots, or `--content` on `buzz messages send`.

## Workflow

### 1. Need a secret?

```
Need credential?
  ├─ Service already holds it (Fly, MC, backend)? → call the service; stop
  ├─ 1Password item exists? → note item NAME; use bundled 1password skill + op run
  ├─ Scoped .env exists? → note FILE PATH only; source in shell
  └─ None of the above? → ask human / 7OPS; do NOT guess or hardcode
```

### 2. Use without exposing

```bash
# GOOD — inject at runtime, output stays local
op run --env-file=.env.template -- ./script.sh

# GOOD — reference only
echo "Using op item: GitHub PAT — Arturito7ei"

# BAD — never do these
echo "$API_KEY"
cat ~/.openclaw/secrets/mc.env
git add .env
```

For `op` sign-in and tmux requirements, follow the bundled `1password` skill exactly.

### 3. Before commit / publish

Run this mental checklist (or grep staged files):

- [ ] No `sk-`, `ghp_`, `gho_`, `xox`, `AKIA`, PEM blocks, or `BEGIN PRIVATE KEY`
- [ ] No `.env` / `*.pem` / `credentials.json` staged
- [ ] No `os.environ.get('SECRET', 'fallback')` in new code — fail closed instead
- [ ] Buzz/PR/issue text mentions item **names** only

Trailofbits patterns to flag: `references/fallback-secrets.md`, `default-credentials.md` in [trailofbits/skills](https://github.com/trailofbits/skills) (`plugins/insecure-defaults/`).

### 4. Suspected leak

1. **Stop** — do not retry with the same value.
2. **Report to 7OPS** with: what leaked, where (channel/file/commit), item name — not the value.
3. **Human rotates** — operator revokes and re-issues; you update references only.
4. Log incident path to `7Ei_OS/security/` or vault errata — names and timestamps only.

## Insecure Defaults (audit lens)

Report when code **runs** with a known fallback secret:

| Pattern | Verdict |
|---|---|
| `os.environ.get('KEY', 'dev-secret')` used for signing/session | **Fix** — require env or crash |
| `process.env.PASS \|\| 'admin123'` in production path | **Fix** |
| Test fixtures with literal secrets in `tests/` only | OK if scoped to tests |
| Per-boot random default for cache key | OK — not security context |

Decisive question (from trailofbits): does the app **run** with the default, or **crash** without config? Running = vulnerable.

## Escalation

| Situation | Escalate to |
|---|---|
| New vendor / SaaS secret store | Arturito (Precedence 01) |
| Production rotation | 7OPS → operator |
| Agent pasted a secret in Buzz | 7OPS immediately; redact thread if possible |
| Need new 1Password item | Human creates item; agent gets name only |

## Output (what agents produce)

- Configuration that references `op` item names or env var **names**
- Audit notes listing file paths and patterns found — redacted excerpts only
- Blocker messages: *"Need op item `<name>` — cannot proceed without human provisioning"*

Never produce: raw tokens, base64 secrets, full env dumps.

## Quality Checklist

- [ ] Referenced secret by name/path only in all published text
- [ ] Used `op run` / inject or service API — not manual paste
- [ ] Staged diff scanned for secret patterns
- [ ] Fallback-secret antipatterns flagged if seen in review
- [ ] Rotation request sent to human if leak suspected

## Examples

**Good — Buzz message**

> Configured `gh` using op item `GitHub PAT — Arturito7ei`. Auth verified with `gh auth status`.

**Bad — Buzz message**

> Here's the token: `ghp_abc123…`

**Good — commit / PR**

> Adds BYOK hook; expects `OPENAI_API_KEY` from op item `OpenAI — 7Ei dev`.

**Bad — code**

```python
SECRET = os.environ.get("JWT_SECRET", "change-me-in-production")
```

## Known Limitations

- Cannot prevent a determined human from pasting secrets — skill binds **agents**.
- `op` desktop integration requires unlocked 1Password app (see bundled skill).
- Pre-commit hooks may not catch all secret formats — manual checklist still required.
- Does not replace 7OPS allowlist review for connector skills (pairs with future `connectors-invoke`).

## Attribution

Insecure-default detection patterns adapted from Trail of Bits [insecure-defaults plugin](https://github.com/trailofbits/skills/tree/main/plugins/insecure-defaults) (CC-BY-SA-4.0). Rewritten for 7Ei RACI, Buzz, and vault paths — not a verbatim import.
