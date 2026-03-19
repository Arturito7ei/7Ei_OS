# Agent Onboarding — First Session Checklist

## For a New Agent Instance

When spawning a new 7Ei agent, complete these steps:

### 1. Define Identity (Layer 2)
- [ ] Create `agents/{instance}/AGENT.md` using `identity/template.md`
- [ ] Create `agents/{instance}/config.yaml` with runtime settings
- [ ] Define skill subset from the skill library

### 2. Inherit Protocols (Layer 0)
- [ ] Read all files in `7Ei_OS/protocols/`
- [ ] Understand the 5-layer knowledge model (`ARCHITECTURE.md`)
- [ ] Acknowledge governance tiers

### 3. Load Organization Knowledge (Layer 1)
- [ ] Read `platform/org/7ei.yaml` for company structure
- [ ] Read `memory/long-term.md` for stable facts
- [ ] Note shared tool config (Jira keys, vault IDs, repo URLs)

### 4. Set Up Memory (Layer 2-4)
- [ ] Initialize personal section in `memory/long-term.md`
- [ ] Verify access to `memory/recent.md` and `tasks/lessons.md`
- [ ] Create initial knowledge card (`identity/knowledge-card.md`)

### 5. Connect to Projects (Layer 3)
- [ ] Read each assigned project's `CLAUDE.md`
- [ ] Load project-specific `.claude/rules/`
- [ ] Note project team composition and your role

### 6. Verify
- [ ] Can read and write to all memory files
- [ ] Can access required integrations
- [ ] First task completes successfully with correct protocol adherence

## For a New Project Repo

When adding 7Ei_OS support to a new codebase:

### 1. Create Minimal CLAUDE.md (Layer 3 only)
```markdown
# {Project Name} — CLAUDE.md

## Operating System
Follow all protocols from 7Ei_OS (github.com/Arturito7ei/7Ei_OS).

## This Project
- Tech stack: {stack}
- Deploy: {how}
- Conventions: {project-specific rules only}
```

### 2. Add Project-Specific Rules
- [ ] Create `.claude/rules/` with repo-specific rules only
- [ ] Do NOT duplicate OS protocols — reference them

### 3. Initialize Project Memory (if needed)
- [ ] Add project entry to `memory/project.md` in agent repo
- [ ] Create project directory in `projects/{name}/` if significant

## Verification Question

After onboarding, the agent should be able to answer:
> "If I learn something new, which layer does it belong to and where do I store it?"

If they can answer this correctly for 5 different examples, onboarding is complete.
