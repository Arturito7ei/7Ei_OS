# Secrets Management

> How API keys, tokens, and credentials are handled.

## Rules

1. **Never commit secrets to any repository** — not even private ones
2. **Never pass secrets in URLs** — query parameters are logged everywhere
3. **Never log secrets** — sanitise all log output
4. **Never hardcode secrets** — always use environment variables or secret stores
5. **Never share secrets in chat** — use secure channels only

## Where Secrets Live

| Secret type | Storage | Access |
|-------------|---------|--------|
| LLM API keys (production) | Fly.io secrets | Backend only |
| LLM API keys (per-org) | Database `deployConfig` column (encrypted) | Backend reads at runtime |
| GitHub tokens | GitHub repo secrets | CI/CD only |
| Clerk auth keys | Fly.io secrets | Backend only |
| Database credentials | Fly.io secrets | Backend only |
| OAuth tokens | Database `oauthTokens` table | Backend, auto-refreshed |
| Vercel tokens | GitHub repo secrets | CI/CD only |

## Rotation Policy

- **Immediately** if a secret is suspected compromised
- **Quarterly** for all production API keys
- **On employee/collaborator departure** — rotate everything they had access to

## For Agents

- Agents never see raw secrets — they call services that use secrets internally
- If an agent needs to configure an API key (e.g., BYOK), it stores it via a dedicated endpoint that encrypts at rest
- Agents must never include secrets in commit messages, PR descriptions, or chat logs
