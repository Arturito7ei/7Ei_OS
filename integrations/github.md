# GitHub Integration

Repository map, permissions model, and automation for the 7Ei GitHub organization.

## Organization

- **Org:** [Arturito7ei](https://github.com/Arturito7ei)
- **Owner:** arturito@7ei.ai
- **Default visibility:** Private (see `standards/repo-conventions.md`)

## Repository Map

| Repo | Purpose | Visibility | Tech Stack |
|------|---------|-----------|------------|
| `7Ei_OS` | Agent operating system — protocols, architecture, standards | Private | Markdown |
| `7ei-mission-control-v2` | Mission Control platform (full-stack) | Private | Next.js 16, React 19, TypeScript, SQLite |
| `Open7Ei-MC` | Mission Control landing/UI | Private | React 18, Vite 6, JavaScript |
| `7EiBank` | Decentralised central bank for AI agents | Private | Documentation + architecture |
| `7EiAI-Website` | 7Ei company website | Private | TBD |
| `Arturito7ei` | GitHub profile + agent identity repo | Public | Markdown |
| `skill-library` | Shared agent skills (open-source) | Public | Bash, Markdown |

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
- `7ei-mission-control-v2`: Vercel auto-deploy from `main`
- `Open7Ei-MC`: Vercel auto-deploy from `main`
- Other repos: manual deploy or pending CI setup

## Security Rules

1. Never commit `.env` files or credentials
2. Never publish private repo URLs publicly
3. Never change repo visibility without human approval
4. Use branch protection — never bypass with `--force`
5. Rotate API tokens if compromised — notify human immediately
