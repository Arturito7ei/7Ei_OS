# Lessons Learned

Capture mistakes, insights, and patterns. When a lesson proves durable (stable 7+ days, seen 3+ times), promote it to a protocol or standard.

## Format

```
### [DATE] — [SHORT TITLE]
**Context:** What was happening
**What went wrong / What we learned:** The insight
**Rule:** The durable takeaway (if promoted)
**Status:** active | promoted to [protocol] | retired
```

---

### 2026-03-24 — Claude Code sessions get stuck on commit step
**Context:** Sprint 3 code session completed all 6 work orders (152 turns) but hung when trying to git commit/push.
**What we learned:** Long-running Claude Code sessions can exhaust their tool allowance or hit permission blocks at the commit step. The work is done but not saved.
**Rule:** Always check on Claude Code sessions after ~100 turns. If stuck, send a follow-up message to retry the commit.
**Status:** active

### 2026-03-24 — Permission prompts block remote operation
**Context:** Tried to operate fully from phone but Claude Code and Dispatch kept hitting tool permission prompts that require clicking on the Mac.
**What we learned:** Each tool (Bash, Read, Write, Edit, Glob, Grep + each MCP integration) prompts "Always Allow" on first use. Must do a permissions sweep at the Mac before going mobile.
**Rule:** When setting up a new machine or new session type, run a permissions sweep first — trigger every tool with a harmless read-only call and click Always Allow on each.
**Status:** active

### 2026-03-24 — Sprint plans should live in the OS repo, not project repos
**Context:** Sprint execution plans were pushed to the Mission Control repo as loose files. But they contain workflow metadata (model recommendations, effort estimates) that belongs to the OS layer, not the project layer.
**What we learned:** Sprint plans are operational knowledge, not project code. They belong in 7Ei_OS/projects/{project}/sprints/.
**Rule:** Sprint execution plans go in 7Ei_OS. Project repos only contain CLAUDE.md (technical spec) and the code itself.
**Status:** active
