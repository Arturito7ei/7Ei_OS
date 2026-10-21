# GitHub Integration

Repository map, permissions model, and automation for the 7Ei GitHub organization.

## Organization

- **Org:** [Arturito7ei](https://github.com/Arturito7ei)
- **Owner:** arturito@7ei.ai
- **Default visibility:** Private (see `standards/repo-conventions.md`)

## Repository Map

Observed 2026-10-21. There is no repo named `7ei-mission-control-v2`. The Mission Control product is `7Ei-Mission_Control_App`. Work selection follows `memory/CLAUDE.md`, not this table.

### Working

| Repo | Purpose | Visibility | May an agent build? |
|------|---------|------------|---------------------|
| `7Ei_OS` | Layer 0 — protocols, board, skills | Public | Board and protocol PRs only |
| `7Ei-MC_TARCO` | Layer 1 vault | Private | Own memory namespace only |
| `silver-board` | Consultation room | Private | Only when the owner asks |
| `silver-board-site` | Public static demo of the room | Public | Only when the owner asks |
| `silver-squeeze` | COMEX early-warning prototype | Public | No. Personal prototype |
| `7Ei-Mission_Control_App` | Virtual office. Web at app.7ei.ai | Public | No. Paused since 2026-08-29 |

### Closed until further notice

| Repo | Purpose | Visibility |
|------|---------|------------|
| `7EiBank` | Decentralised bank concept | Private |
| `7PolyBet` | Personal Polymarket dry-run | Private |

### Do not resume

Dormant since March–June 2026 unless the owner names one: `Open7Ei-MC`, `7ei-mission-control`, `7ei-pixel-agents`, `skill-library`, `AgAu`, `AgAu_UNBANK`, `7EiAI-Website`, `7ei-iptv-dashboard`, `openclaw-brain-sync`, `Silversqueezedashboard`, `agent-continuity`, `7Ei-MC_TARCO_Backup`, `7Ei-Mission_Control_Backup`. Profile repo `Arturito7ei` is the GitHub profile, not a product.

## Permissions Model

### Agent Access
| Agent | Access Level | Repos |
|-------|-------------|-------|
| Arturito7EiClaude | Write (via Claude Code) | All repos |
| Arturito7EiClaw | Write (via API/browser) | skill-library, coordination tasks |

### Branch Protection
- `main` branch is protected on all repos
- Direct push to `main` is blocked
- PRs require at least one review (human or orchestrator)
- Status checks must pass before merge (where CI is configured)

## Branch Strategy

### Agent Branches
```
claude/<description>-<session-id>
```
- Always branch from `main`
- One branch per task or session
- PR back to `main` when complete
- Delete branch after merge

### Push Protocol
```bash
git push -u origin claude/<branch-name>
```
- Always use `-u` flag on first push
- If push fails due to network, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
- Never force-push to shared branches without human approval

## GitHub CLI (`gh`)

Agents use `gh` for GitHub operations:

```bash
# Create PR
gh pr create --title "scope: description" --body "Summary and test plan"

# View PR
gh pr view 123

# List issues
gh issue list

# View checks
gh pr checks 123

# API calls
gh api repos/Arturito7ei/7Ei_OS/pulls
```

## Automation

### PR Templates
Repos with PR templates (`.github/pull_request_template.md`) auto-populate PR descriptions. Follow the template structure.

### Issue Templates
Use issue templates when available:
- Bug reports: `.github/ISSUE_TEMPLATE/bug_report.md`
- Feature requests: `.github/ISSUE_TEMPLATE/feature_request.md`

### CI/CD
- `7Ei-Mission_Control_App`: Fly.io backend + Vercel web. Paused. Do not deploy a feature sprint.
- `silver-squeeze`: weekday `market-feeds` ingest, then `pages.yml`. Leave it unless the ingest is broken.
- `silver-board-site`: GitHub Pages static demo.
- Other repos: manual deploy or no deploy.

## Security Rules

1. Never commit `.env` files or credentials
2. Never publish private repo URLs publicly
3. Never change repo visibility without human approval
4. Use branch protection — never bypass with `--force`
5. Rotate API tokens if compromised — notify human immediately
