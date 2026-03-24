# 7Ei OS — Claude Code Guide

> Agent operating system protocols and standards. This repo defines how 7Ei agents think, remember, coordinate, and evolve.

---

## Quick orientation

```
7Ei_OS/
├── protocols/       Memory, governance, coordination, spawning, learning
├── architecture/    Agent template, hierarchy, skill system, knowledge graph
├── standards/       Code review, naming, repo conventions
└── integrations/    GitHub, Jira, Google Workspace, Obsidian
```

**This repo is documentation-only** — no runnable code. Changes here update the agent operating system specification.

---

## Skill / Plugin Routing

| User intent | Skill | Notes |
|---|---|---|
| "review protocol", "check this change" | **code-review** | Review markdown for consistency, completeness |
| "create a new skill", "add a protocol" | **skill-creator** | Scaffold new protocol/skill files |
| "jira ticket", "track this in jira" | **atlassian** | Link OS changes to Jira |
| Complex multi-file protocol updates | **superpowers** | Parallel research across protocols |

### Precedence rules

1. **Most specific wins** — same as Mission Control.
2. **Protocol consistency** — New protocols must follow the format in existing `protocols/*.md` files.
3. **Cross-repo awareness** — Changes here may require matching changes in `7Ei-Mission_Control_App`.
4. **Review before merge** — Always run `code-review` on protocol changes.

---

## Preflight checklist

- [ ] Read the protocol/architecture file before editing
- [ ] Check if the change conflicts with `protocols/principles.md` (immutable principles)
- [ ] Verify naming follows `standards/naming.md`
- [ ] Identify cross-repo impact (does Mission Control need a matching update?)

## Post-change validation

- [ ] Protocol follows existing format (sections, headers, tone)
- [ ] No conflicts with immutable principles
- [ ] Cross-references to other protocols are correct
- [ ] Commit with descriptive message, push to feature branch

---

## Safety rules

- **Never** modify `protocols/principles.md` without explicit user approval — these are immutable.
- **Never** delete protocols — deprecate them with a note instead.
- **Never** expose internal agent configurations or secrets.
- **Ask** before making changes that affect the agent hierarchy or governance tiers.

---

*Last updated: March 2026 · 7Ei OS*
