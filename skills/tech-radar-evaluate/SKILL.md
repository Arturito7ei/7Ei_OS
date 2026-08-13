---
name: tech-radar-evaluate
description: Evaluate a tool, dependency, or skill candidate for 7Ei using the sovereignty-first rubric. Use before adopting libraries, importing skills, starting trials, or recommending stack changes. Produces adopt/trial/hold/avoid with citations.
---

# Tech Radar Evaluate

Score tools, processes, and skill packs before 7Ei adopts them. Output is decision-ready: verdict + evidence + escalation flags.

**Cluster:** Research  
**Owner:** 7RD  
**Canonical rubric:** `~/.buzz/RESEARCH/RD_SCREENING_STRATEGY_2026_08_13.md` §4  
**Queue:** append scored rows to `~/.buzz/RESEARCH/RD_CANDIDATE_QUEUE.md`

## When to Use

- A human or agent proposes a new tool, CLI, skill pack, SaaS, or process pattern
- Before `npx skills add`, copying a vendor `SKILL.md`, or binding a skill fleet-wide
- Before recommending stack migration, new vendor spend, or replacing an existing tool
- Weekly radar hour: batch-triage candidates from `RD_CANDIDATE_QUEUE.md`

## Inputs

Collect before scoring:

| Input | Required |
|---|---|
| Candidate name + URL or repo path | Yes |
| Problem statement for 7Ei | Yes (or mark "no problem — drop") |
| Version / `pushed_at` / release date | Yes if external; note if unread |
| License | Yes for imports |
| Who requested / which cluster | Yes |

Check local first: `~/.buzz/RESEARCH/`, vault `03-Research/`, `Skill-Library/`, existing `7Ei_OS/skills/catalog.md`.

## Rubric (order is load-bearing)

Score in this order. **Stop early on hard fail.**

### 1. Problem fit

Does 7Ei have a real job for this *now*? Thin cluster or open wound beats speculative future need.

- No problem → **drop** (do not queue) or **Hold** with re-score date
- Duplicate of vault/7Ei_OS SoT → **Hold** or **Avoid** (point at existing)

### 2. Precedence 01–03 (hard gate)

From vault `Company/Principles-Handbook.md` — Hierarchy of Precedence:

| # | Principle | Fail signal |
|---|---|---|
| 01 | Sovereignty + Data Control | Mandatory cloud, tool-broker, data leaves operator control |
| 02 | Human Interest > Machine Interest | No human override path |
| 03 | Individual Rights > Democratic Consensus | Privacy/residency violation without explicit consent |

**Fail → Avoid** (or escalate to Arturito before any Trial). Log the precedence number.

### 3. Sovereignty

| Signal | Score |
|---|---|
| Self-hostable / local files / BYOK | Pass |
| Optional SaaS with local fallback | Trial only with Thierry gate if paid/residency |
| Mandatory SaaS / external tool broker (e.g. Zero plugins) | **Avoid** |

### 4. Maturity

Stars alone insufficient. Record:

- Version or last push date (`gh api`, npm, PyPI — cite command output)
- Maintainer health (release cadence, open critical issues)
- License compatibility
- For skills: `SKILL.md` quality, scripts reviewed for network/secret exfil

Mark **verified** (you ran/read primary source) vs **read** (secondary only).

### 5. Migration / exit

- Can we delete it without rewriting the org?
- Per-skill cherry-pick vs bulk `--all` install?
- CC-BY-SA or other share-alike on derivatives?

### 6. Removes what?

Name the habit, tool, or ambiguity this kills. Additive-only adoption is a smell — say what it replaces.

### 7. Context cost

Tokens, MCP sprawl, always-on tools, mega-pack default load. Prefer named skill bind over pasting into every agent `core`.

### 8. Verdict

| Verdict | Meaning |
|---|---|
| **Adopt** | Author/adapt into `7Ei_OS/skills/` or `GUIDES/`; update catalog + sync |
| **Trial** | Time-boxed ≤14 days; one owner; one agent or channel; kill criteria required |
| **Hold** | Valid later or wrong cluster priority; set re-score trigger |
| **Avoid** | Disqualified — cite precedence or sovereignty reason |

## Output Format

Write to `~/.buzz/RESEARCH/` (or append queue row) using this template:

```markdown
## [Candidate name]

**Verdict:** Adopt | Trial | Hold | Avoid  
**Scored:** YYYY-MM-DD by [agent]  
**Citations:** [URL/path + version/date]  
**Verified vs read:** [what you ran vs what you read]

| # | Criterion | Finding |
|---|-----------|---------|
| 1 | Problem fit | … |
| 2 | Precedence 01–03 | … |
| 3 | Sovereignty | … |
| 4 | Maturity | … |
| 5 | Migration/exit | … |
| 6 | Removes what? | … |
| 7 | Context cost | … |

**Escalations:** [7MAN / Arturito / 7OPS / Dev — or none]

**Next action:** [queue row update / author SKILL.md / trial plan / none]
```

Update `RD_CANDIDATE_QUEUE.md` stage + verdict columns in the same turn.

## Escalation Matrix

| Trigger | Escalate to |
|---|---|
| Precedence 01–03 exception or residency | Arturito |
| Stack migration, new vendor, new spend | 7MAN |
| Trial touches credentials, network, connectors | 7OPS (Consult) |
| Process skill touching code/PR workflow | Dev (Consult) |
| Promote draft → active strategy change | 7MAN |

## Hard Rules

- **No** `npx skills add <mega> --all` or bulk mega-pack defaults
- **No** fleet bind during Trial — trial is one agent or one channel
- **No** unsupported claims — every recommendation needs URL, path, version, or command output
- **No** growing every agent `core` with full skill text — point, then load on demand
- Paid / SaaS / residency-sensitive → Thierry before Trial

## Adopt Path (when verdict = Adopt)

1. Author `7Ei_OS/skills/<name>/SKILL.md` (agentskills.io frontmatter)
2. Update `7Ei_OS/skills/catalog.md`
3. Run `OBSIDIAN_VAULT=/path/to/vault python3 skills/sync_vault.py`
4. PR to `7Ei_OS`; announce in `#knowledge` + `#research` with path + who should bind

## Example (abbreviated)

**Candidate:** `vercel-labs/skills` CLI

| # | Finding |
|---|---------|
| 1 | Problem: per-skill install friction — yes |
| 2 | Local install; no mandatory broker — pass |
| 3 | Self-hostable SKILL.md dirs — pass |
| 4 | npm `skills@1.5.22`, pushed 2026-08-05 — verified via npm |
| 5 | Exit = delete installed dirs — low cost |
| 6 | Removes manual clone/copy friction |
| 7 | Low if cherry-pick; high if `--all` — forbid `--all` |

**Verdict:** Trial (installer only). **Next:** `npx skills add … --list`, cherry-pick one skill, trial note in RESEARCH.

## Quality Checklist

- [ ] Rubric order followed; early stop documented if applicable
- [ ] Every claim has citation with version/date
- [ ] Verified vs read distinguished
- [ ] Verdict is exactly one of adopt/trial/hold/avoid
- [ ] Queue row updated (or drop reason recorded)
- [ ] Escalations named or explicitly "none"

## Known Limitations

- Does not execute installs or spend — produces decision artifacts only
- Does not override Arturito on Precedence 01–03
- GitHub metadata can drift — re-verify `pushed_at` before Trial/Adopt promotion
