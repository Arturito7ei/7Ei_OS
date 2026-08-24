---
name: gauntlet-loop
description: >-
  Turns a creative deliverable goal into a paste-ready gauntlet prompt: concrete
  quality bar, builder+critic per piece, blind A/B vs the bar, loop until win.
  Use for landing pages, explainers, dashboards, OUTBOX docs — not routine Buzz
  ops, radar scoring, or PR work. Triggers on "gauntlet loop", "gauntlet this",
  "loop until it beats X", or explicit skill bind.
disable-model-invocation: true
---

# Gauntlet Loop

**Attribution:** Technique by [Matt Shumer](https://github.com/mshumer/Claude-of-Duty) · packaged by [RoboNuggets](https://github.com/robonuggets/gauntlet-loop) · CC BY 4.0  
**Cluster:** Research / Strategy  
**Owner:** 7RD  
**Pairs with:** Cursor `loop` skill, `Task` subagents  
**Do not use for:** `tech-radar-evaluate`, `investigate`, default Buzz channel turns, sovereignty decisions

The user gives a **goal**. You return ONE short prompt they can paste into a fresh agent session — or run it yourself when they say "run it".

You are not doing the work (yet). You are writing the prompt that makes another agent grind until it beats a real reference.

## Flow

1. **Read the goal.** Restate internally; do not echo on screen.
2. **Set the bar.** If the user supplied a reference, use it. Otherwise offer **2–3 candidate bars** (one line each) and **stop**. Wait for their pick. Do not write the prompt yet.
3. **Write the prompt.** One block, paste-ready, no preamble, no headings inside, no narration after.
4. **Offer to run it.** One flat line under the prompt: `I can run this here.` Not a question.

If they say run it, you become the lead agent and follow the prompt you just wrote.

## The bar is the whole trick

Everything else is scaffolding. The loop only produces quality if the comparison target is real.

A bar must pass three tests:

- **Named** — specific thing, not a category. "Stripe's pricing page" works. "Award-winning SaaS sites" does not.
- **Fetchable** — critic can obtain it (live URL, published piece, repo, benchmark). If unobtainable, the critic hallucinates the comparison.
- **Comparable** — side-by-side blind A/B is imaginable.

| Goal type | Bar that works |
|---|---|
| Website, app, UI, dashboard | Live site of a named best-in-class product, same viewport |
| Writing | Specific published piece, same length and format |
| Code, tooling | Named repo + its benchmark or test suite |
| Research | Named analyst report or paper methods section |
| Deck, doc | Real artifact from a firm known for it |

When proposing bars, prefer the hardest one the agent can genuinely reach.

If the goal has a measurable half (load time, pass rate, word count), name it alongside the reference.

## 7Ei prompt template (Cursor)

Adapt wording every time. Fill brackets; keep ~120–180 words; plain sentences, no bullets inside the prompt.

```
Build [GOAL].

The bar is [BAR]. Get the real thing first and compare against it directly, not against a description of it.

Break this into the smallest pieces that can be improved and judged on their own. For each piece, fan out a builder and a separate critic with fresh context. The critic inspects the actual output, puts it next to the bar blind with the labels stripped, says which one is better, and names the single biggest remaining gap. Then it goes back to the builder.

The critic should be a harsh critic. Praise is not useful. If ours does not win, it keeps going.

Loop on each piece until the critic picks ours blind. Do not stop before that. Use Cursor Task subagents for parallel builders and critics; use the loop skill for recurring piece passes.

Keep a live progress artifact updating as the work evolves (Buzz canvas, `.scratch/`, or committed file).

Run builders and critics as parallel subagents with fresh context each round.
```

Rules for what you fill in:

- Bake the bar in as a concrete, fetchable thing (URL, product name, repo, title).
- Add a budget or round ceiling **only if the user named one**. No default cap — token burn is unbounded otherwise.
- Add tool names only if the goal needs them (browser, deploy target, image gen).
- Do not over-specify architecture, file layout, or stack unless the user demanded it.

## Cursor portability

| Upstream (Claude Code) | 7Ei equivalent |
|---|---|
| `/loop` | `~/.cursor/skills-cursor/loop/SKILL.md` |
| `ultracode` / fan-out | Cursor `Task` subagents |
| Progress page | Buzz canvas, `.scratch/`, or repo artifact |
| Fresh critic | Separate subagent invocation per round |

## When to activate

**Yes:** OUTBOX explainers, landing pages, polished research briefs, visual dashboards with a named reference bar.

**No:** Weekly radar scoring (`tech-radar-evaluate`), bugfix/PR work (`investigate`), channel coordination, anything needing human sovereignty gates.

## Guardrails

- Human stop always valid — never argue to continue past budget.
- Never auto-run on channel pickup; explicit opt-in only.
- Kill if critic cannot fetch the bar (hallucinated comparison).
- Kill if token burn >2× single-pass baseline with no quality lift.

## What breaks a gauntlet loop

- **Vague bar** — critic invents comparison and approves everything.
- **Builder judging its own work** — critic must be separate with fresh context.
- **Soft critic** — binary A/B only; no scores out of 10.
- **Named exit after N rounds** — exit is winning the comparison or user stop.
- **Over-specifying** — every extra instruction removes agent judgment.

## Quality checklist

- [ ] Bar is named, fetchable, comparable
- [ ] Prompt is 120–180 words, paste-ready
- [ ] Cursor portability lines present (Task + loop, not ultracode)
- [ ] When-not-to-use cross-refs respected
- [ ] CC BY 4.0 attribution preserved if adapting upstream text

## Example (dashboard)

User: "dashboard for our github rising radar scan data."

Bars: A) GitHub Trending page at-a-glance scanability B) ThoughtWorks Technology Radar track layout C) Vercel dashboard KPI cards. User picks A+B.

```
Build a self-contained HTML dashboard for 7Ei GitHub Rising Radar scan data — climbers, star velocity, track segmentation, scan metadata.

The bar is GitHub Trending's at-a-glance repo cards plus ThoughtWorks Technology Radar's track clarity. Open github.com/trending and radar.thoughtworks.com and compare our dashboard against them directly, not against a description.

Break into judgeable pieces: summary KPIs, climber delta chart, track tabs, repo detail cards, mobile layout. For each piece, fan out a builder and a separate critic with fresh context. The critic opens our dashboard and the live references side by side blind, says which communicates rising-repo signal faster, and names the single biggest remaining gap.

The critic should be a harsh critic. Praise is not useful. If ours does not win, it keeps going.

Loop on each piece until the critic picks ours blind. Use Cursor Task subagents and the loop skill for piece passes. Keep progress in RESEARCH/ or the skill's dashboard/ dir.

Run builders and critics as parallel subagents with fresh context each round.
```
