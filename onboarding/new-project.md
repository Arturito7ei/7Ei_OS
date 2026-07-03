# Onboarding a new PROJECT repo

(For onboarding an AGENT, see `README.md`.) Adding 7Ei_OS support to a codebase:

1. **Minimal root `CLAUDE.md`** (Layer 3 only — keep it <70 lines):

```markdown
# {Project} — root guide

## Layer 0 — 7Ei OS
Follow all protocols from 7Ei_OS (github.com/Arturito7ei/7Ei_OS).
Shared knowledge: vault Arturito7ei/7Ei-MC_TARCO.

## This project
- Tech stack / deploy / conventions: {project-specific only}
```

2. **Layer, don't bloat**: subsystem conventions go in per-directory `CLAUDE.md` files (`backend/CLAUDE.md`, `web/CLAUDE.md`, …) which load on demand; path-scoped rules in `.claude/rules/`. State goes in `STATUS.md`, never in CLAUDE.md. Reference OS protocols — never duplicate them.
3. **Interop**: if non-Claude tools work in the repo, keep `AGENTS.md` and have `CLAUDE.md` import it (`@AGENTS.md`).
4. **Memory**: add the project to `projects/` here if significant; milestones mirror to the vault.

Reference implementation: `Arturito7ei/7Ei-Mission_Control_App` (layered CLAUDE.md, HANDOFF.md kickoff, STATUS.md convention).
