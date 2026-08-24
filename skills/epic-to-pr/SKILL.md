---
name: epic-to-pr
description: Turn an epic or venture slice into hypothesis, task breakdown, Buzz issues/PR with channel link, and done criteria. Use when staffing work from research, 777 gate, or multi-day engineering. Default board is GitHub Issues — Jira only when 7DEV chooses per venture.
---

# Epic to PR

Ship work from **epic intent → scoped tasks → branch/PR → review → merge** without losing channel context or duplicating boards.

**Cluster:** Project-Management  
**Owner:** 7DEV (author: 7RD)  
**Canonical process:** `~/.buzz/GUIDES/ENGINEERING_PROCESS_EPIC_TO_PR.md`  
**Inspired by:** deanpeters `epic-hypothesis` (patterns only — read LICENSE before any verbatim import)  
**Sovereignty:** Buzz + GitHub BYOK; Jira optional per venture, never dual-primary with GitHub.

## When to Use

- Multi-day work needs an epic/story before coding starts
- Research or 777 gate produces a venture slice to staff
- Opening a Buzz-hosted repo issue or PR that must link back to the originating channel
- Breaking an epic into stories with clear done-when criteria
- Choosing GitHub Issues vs Jira for a venture (document on channel canvas)

## When Not to Use

- Single-line fix or typo — just PR
- Work already tracked with a primary ticket elsewhere — link, do not re-home
- Jira **and** GitHub Projects as dual SoT for the same epic

## Inputs

| Input | Required |
|---|---|
| Epic title + one outcome | Yes |
| Venture / channel UUID | Yes for Buzz issues & PRs |
| Repo (local checkout or Buzz repo) | Yes before PR |
| Requester + RACI (who decides) | Yes |
| Done-when for epic | Yes |

Check first: venture channel canvas, existing issues/PRs, `GUIDES/ENGINEERING_PROCESS_EPIC_TO_PR.md`.

## Workflow

### 1. Hypothesis (epic one-liner)

Write in this shape (deanpeters `epic-hypothesis` pattern):

```
We believe [change] for [user/agent/system] will [measurable outcome] because [reason].
We will know we succeeded when [evidence / metric / demo].
```

If the hypothesis is weak, stop and ask — do not break into stories yet.

### 2. Epic issue

**GitHub (default):**

```bash
gh issue create --repo <owner/repo> \
  --title "Epic: <title>" \
  --label epic \
  --body "$(cat <<'EOF'
## Hypothesis
...

## Outcome
...

## Done-when
- [ ] ...

## Channel
<buzz-channel-uuid>

## RACI
- Accountable: ...
- Responsible: ...
EOF
)"
```

**Buzz-hosted repo:**

```bash
buzz issues create --repo-owner <hex> --repo-id <id> \
  --title "Epic: <title>" \
  --content "$(cat <<'EOF'
## Hypothesis
...

## Outcome
...

## Done-when
- [ ] ...

## Channel
<buzz-channel-uuid>

## RACI
- Accountable: ...
- Responsible: ...
EOF
)"
```

`buzz issues create` has no `--channel` flag — put the channel UUID in the issue body (same pattern as GitHub). Use the `link` field from the response verbatim in channel posts — never invent HTTPS URLs for Buzz repos.

### 3. Break into stories

Each story needs:

| Field | Rule |
|---|---|
| Title | Verb + object |
| Done-when | Observable, testable |
| Size | Fits one worktree / one PR where possible |
| Labels | `story` or `task`; `dept:dev\|ops\|rd\|man` |

Link stories to epic (GitHub sub-issue or reference epic `#` in body).

### 4. Implement (worktree rule)

```bash
# Never commit on main for multi-file work
git checkout -b <venture>/<story-slug>
# ... implement ...
```

Work in `REPOS/` checkout or Buzz git remote — read repo `AGENTS.md` first.

### 5. Open PR with channel link

**GitHub:**

```bash
gh pr create --title "..." --body "..."
```

**Buzz-hosted (required channel preservation):**

```bash
buzz pr open --repo-owner <hex> --repo-id <id> \
  --subject "..." --body "..." \
  --commit "$(git rev-parse HEAD)" --clone <clone-url> \
  --channel <channel-uuid>
```

Only `buzz pr open` takes `--channel` (NIP-29 h-tag). Announce in channel with the returned `link` field (renders as preview card in Buzz Desktop).

### 6. Review and close

| Step | Who | Rule |
|---|---|---|
| Review | Peer head or operator | No self-merge on Precedence-sensitive paths |
| CI | Implementer | Green before merge |
| Close epic | 7DEV | All stories done; update channel |

## Jira path (optional)

7DEV may choose Jira when multi-sprint hierarchy, external collaborators, or cost tracking requires it.

**If Jira is primary:**

- Document choice on venture channel canvas
- Do **not** mirror the same epic in GitHub Projects
- Agents still post milestones to Buzz channel

## Quality checklist

- [ ] Hypothesis one-liner exists before stories
- [ ] Every story has done-when
- [ ] Buzz PRs pass `--channel <uuid>` when work originated in Buzz; Buzz issues put the channel UUID in the body (no `--channel` on `issues create`)
- [ ] Channel announcement uses Buzz `link` field, not guessed URLs
- [ ] No dual-primary Jira + GitHub for same epic
- [ ] No commits on `main` for multi-day work

## Anti-patterns

- Building without epic/story for multi-day work
- Opening PR without channel link when humans expect traceability
- Inventing `https://` URLs for Buzz-hosted repos
- Dual-homing tickets across Jira and GitHub without declared primary

## Escalation

| Trigger | To |
|---|---|
| Venture board choice (GitHub vs Jira) | 7DEV |
| Precedence-sensitive merge | Peer review or operator |
| Process conflict with repo `AGENTS.md` | 7DEV + 7MAN |

## Examples

**Research → implement skill (this funnel):**

1. Hypothesis: "Weekly radar + chooser reduces wrong skill adoption."
2. Epic in 7Ei_OS or RESEARCH tracker
3. Stories: scan skill, evaluate skill, chooser template
4. PRs with `--channel` from `#research` or founder DM
5. Close when merged + bind note posted

## Known limitations

- Does not replace 7DEV's eng judgment on CI, architecture, or review depth
- Jira integration is manual unless `jira-openclaw` skill is bound for that venture
- Buzz `issues`/`pr` require correct repo ownership and channel membership
