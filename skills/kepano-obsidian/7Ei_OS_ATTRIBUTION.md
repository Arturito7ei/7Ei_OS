# Attribution — kepano/obsidian-skills

> **Origin:** https://github.com/kepano/obsidian-skills  
> **Author:** Steph Ango (kepano)  
> **License:** MIT (inherited from upstream repo)
> **Integrated into 7Ei_OS:** 2026-06-23 via Option 1A (Fork & Adapt)

## What Was Copied

The `skills/` directory contains 5 agent-ready skills from the upstream repository:

| Skill | File |
|-------|------|
| obsidian-markdown | `skills/obsidian-markdown/SKILL.md` |
| obsidian-bases | `skills/obsidian-bases/SKILL.md` |
| json-canvas | `skills/json-canvas/SKILL.md` |
| obsidian-cli | `skills/obsidian-cli/SKILL.md` |
| defuddle | `skills/defuddle/SKILL.md` |

## What Was Modified

- **Removed `.git/`** — merged into 7Ei_OS monorepo (no submodules)
- **Removed `README.md`** (upstream install instructions not needed inside 7Ei_OS)
- **Registered in `7Ei_OS/skills/catalog.md`** — for Obsidian vault + workspace symlink generation
- **Adapted vault paths** (if any) to point to `TARCO-MC_Vault`

## How to Update from Upstream

```bash
cd ~/Developer/7Ei_OS
# Manual upstream sync (kepano may add new skills or fix content)
git clone --depth 1 https://github.com/kepano/obsidian-skills.git /tmp/kepano-latest
# Review diffs, copy skills/ folder, preserve ATTRIBUTION.md
git diff --stat
# Commit with tag: `sync(kepano): pull upstream changes`
```

## Why Fork Instead of Submodule

- **Atomic versioning** — 7Ei_OS commits include all skills, no broken references
- **Offline resilience** — agents work with local files, no Git dependency
- **Simpler CI/CD** — no `--recurse-submodules` needed for clone/build
- **7Ei-specific adaptations** — vault paths, memory tiers, etc. can diverge safely
