# Changelog

All notable changes to 7Ei_OS are documented here. This is the evolution log of the agent operating system.

Format: `[version] - YYYY-MM-DD`

---

## [0.2.0] - 2026-03-19

### Added
- `protocols/coordination.md` — multi-agent coordination, heartbeats, task handoff
- `protocols/spawning.md` — how to create new agent instances from the Arturito7EiT template
- `protocols/session-continuity.md` — boot sequence, memory consolidation, session handoff
- `architecture/agent-template.md` — the Arturito7EiT primordial DNA
- `architecture/agent-hierarchy.md` — template → instance → specialization model
- `architecture/skill-system.md` — skill domains, composability, the shared skill library
- `architecture/knowledge-graph.md` — Obsidian vault integration, research pipeline
- `standards/code-review.md` — universal code review checklist
- `standards/naming.md` — naming conventions for agents, repos, branches
- `standards/repo-conventions.md` — repo defaults, visibility, commit style
- `integrations/obsidian.md` — vault structure, MCP, sync strategy
- `integrations/jira.md` — Jira configuration, project spaces, automation
- `integrations/github.md` — repo map, permissions model, branch strategy
- `integrations/google-workspace.md` — Google integration map
- `CONTRIBUTING.md` — how agents propose OS changes via PR
- Documented Arturito7EiClaw as second active agent instance

### Changed
- Restructured repo to new canonical layout (protocols, architecture, standards, integrations)
- Rewrote `README.md` for agent-first consumption
- Updated `protocols/memory.md` — distilled to clean agent-consumable format
- Updated `protocols/governance.md` — expanded approval tiers and audit trail

## [0.1.0] - 2026-03-15

### Added
- Initial protocol definitions (memory, workflow, learning, principles, governance, knowledge-boundaries)
- 5-layer knowledge architecture (`ARCHITECTURE.md`)
- Agent identity template and knowledge card system
- Bootstrap onboarding checklist
- Knowledge sync strategy (reference, embed, submodule)
