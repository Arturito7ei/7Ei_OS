# Audit Trail

> Everything significant gets logged. Nothing important gets lost.

## What Gets Logged

| Event | Where | Retention |
|-------|-------|----------|
| Agent decisions (above Level 1) | `memory/lessons.md` | Permanent |
| Permission changes | Git commit history | Permanent |
| Deployments | GitHub Actions logs | 90 days |
| Data access (cross-org) | Application logs | 1 year |
| Sprint completions | `projects/{name}/sprints/` | Permanent |
| Protocol changes | Git commit history + CHANGELOG.md | Permanent |
| Security incidents | `memory/lessons.md` + dedicated incident file | Permanent |

## Log Format

```
[DATE] [AGENT] [ACTION] [RESULT] [APPROVER]
```

Example:
```
2026-03-24 arturito-dispatch merge-pr approved arturito-human
2026-03-24 claude-code deploy-backend success github-actions
2026-03-24 arturito-dispatch create-issues completed auto
```

## Review Cadence

- **Per sprint:** Review lessons.md for patterns
- **Monthly:** Review permission usage and remove unused
- **Quarterly:** Full security audit of agent access
