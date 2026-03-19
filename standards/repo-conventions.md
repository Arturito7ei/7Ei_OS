# Repository Conventions

Default rules for all 7Ei repositories.

## Visibility

**Private by default.** All 7Ei repos are private unless explicitly decided otherwise.

| Repo | Visibility | Rationale |
|------|-----------|-----------|
| `7Ei_OS` | Private | Internal operating system |
| `7ei-mission-control-v2` | Private | Core platform |
| `Open7Ei-MC` | Private | Platform UI |
| `7EiBank` | Private | Financial product |
| `7EiAI-Website` | Private | Company website |
| `Arturito7ei` | Public | GitHub profile (README only) |
| `skill-library` | Public | Shared skills — open-source (MIT) |

Public repos require human approval before creation or visibility change.

## Branch Strategy

### Protected Branches
- `main` — production-ready code. Never push directly.
- Merges to `main` require PR + review.

### Feature Branches
```
claude/<description>-<session-id>
```
- One branch per task or session
- Branch from `main`, PR back to `main`
- Delete branch after merge

### Never Do
- Force-push to `main`
- Push directly to `main` without PR
- Create branches without the `claude/` prefix (for agent work)
- Leave stale branches (clean up after merge)

## Commit Style

### Format
```
<scope>: <imperative description of change>
```

Keep the first line under 72 characters. Add a blank line and body for complex changes.

### Rules
- Use imperative mood: "add feature" not "added feature"
- Explain **why**, not just **what**
- One logical change per commit — don't bundle unrelated changes
- Never commit secrets, `.env` files, or credentials
- Never skip pre-commit hooks (`--no-verify`)

## Required Files

Every 7Ei repo should have:

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Platform instructions for agents working on this repo |
| `.gitignore` | Ignore `.env`, `node_modules/`, OS files, IDE config |
| `README.md` | What this repo is, how to use it |

### CLAUDE.md Structure

Keep it thin — reference `7Ei_OS` for protocols, only add project-specific rules:

```markdown
# {Project Name} — Claude Code Instructions

## Operating System
Follow all protocols from 7Ei_OS (github.com/Arturito7ei/7Ei_OS).

## This Project
- **Purpose:** {what this repo does}
- **Tech stack:** {stack}
- **Deploy:** {how}
- **Commands:** {build, test, dev}

## Conventions
{Project-specific rules ONLY — do not duplicate OS protocols}
```

## .gitignore Baseline

Every repo must ignore at minimum:

```
.env
.env.*
node_modules/
.DS_Store
*.log
.idea/
.vscode/
*.swp
```

## Pull Request Standards

### PR Title
- Under 72 characters
- Prefixed with scope: `os: add coordination protocol`

### PR Body
```markdown
## Summary
- What changed and why (1-3 bullet points)

## Test Plan
- How to verify the change works
```

### PR Size
- Keep PRs focused — one concern per PR
- Prefer multiple small PRs over one large PR
- If a PR touches more than 10 files, consider splitting it

## Language Standards

- All code comments in English
- All documentation in English
- All commit messages in English
- Currency amounts in CHF unless stated otherwise (7EiBank)
