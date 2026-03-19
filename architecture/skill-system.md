# Skill System

How agents acquire, compose, and share capabilities.

## What Is a Skill

A skill is a packaged capability that any agent can load and use, regardless of runtime. Each skill contains:

```
skill-name/
├── SKILL.md           # Skill definition — when to use, how to use, red flags
├── scripts/           # Helper scripts the agent can source and execute
└── .env.example       # Required environment variables (never committed)
```

The `SKILL.md` file is the agent's instruction manual. It must be written so that any LLM agent (Claude, GPT, Gemini, open-source) can read it and immediately use the skill.

## Skill Domains

Skills are organized into 6 domains:

| Domain | Purpose | Examples |
|--------|---------|---------|
| **Engineering** | Code, architecture, testing | code-review, refactoring, test-generation |
| **Operations** | Infrastructure, deployment, monitoring | ci-cd, deploy, health-check |
| **Knowledge** | Research, documentation, learning | obsidian-sync, research-pipeline, doc-generation |
| **Communication** | Messaging, notifications, reporting | telegram-notify, status-report, email-compose |
| **Project Management** | Planning, tracking, coordination | jira-openclaw, sprint-planning, task-decomposition |
| **Integration** | External tool connectivity | github-api, google-workspace, mcp-tools |

## Shared Skill Library

**Repository:** [Arturito7ei/skill-library](https://github.com/Arturito7ei/skill-library)

The skill library is a shared repo where all agents can contribute and consume skills.

### Current Skills

| Skill | Domain | Contributed By | Description |
|-------|--------|---------------|-------------|
| `jira-openclaw` | Project Management | Arturito7EiClaw | Manage Jira via REST API — no OAuth browser flow needed |

### Contributing a Skill

1. Create a directory in the skill library: `skill-name/`
2. Write `SKILL.md` with frontmatter (name, description) and full instructions
3. Add helper scripts in `scripts/` if applicable
4. Add `.env.example` for required credentials
5. Open a PR with usage examples and red flags documented

## Skill Composability

Skills can be combined for complex workflows:

```
Example: Sprint Planning Workflow
1. research-pipeline    → Analyze requirements
2. task-decomposition   → Break into actionable tasks
3. jira-openclaw        → Create tasks in Jira
4. sprint-planning      → Organize into sprint
5. status-report        → Generate summary for stakeholders
```

Agents declare their skill subset in `AGENT.md`. The orchestrator routes tasks to agents with the required skills.

## SKILL.md Format

Every skill definition follows this structure:

```markdown
---
name: skill-name
description: One-line description of what this skill does and when to use it.
---

# Skill Name

> Brief purpose statement.

## Why This Skill Exists
{What problem it solves, why existing tools are insufficient}

## Setup
{Environment variables, dependencies, prerequisites}

## When to Use
{Bullet list of scenarios where this skill applies}

## The Process
{Step-by-step instructions with code examples}

## Function Reference
{Table of available helpers with args and descriptions}

## Red Flags
{Common mistakes, anti-patterns, things to never do}

## Integration
{How this skill works with other skills and agents}
```

## Skill Lifecycle

```
Need identified
  → Prototype during a session (ad-hoc scripts)
  → Formalize into SKILL.md + scripts/
  → PR to skill-library
  → Available to all agents
  → Feedback loop: agents report issues via tasks/lessons.md
  → Skill improved via PR
```

## Skill vs Protocol

| | Skill | Protocol |
|--|-------|----------|
| **Scope** | Optional capability | Universal requirement |
| **Lives in** | skill-library | 7Ei_OS |
| **Loaded** | When needed | Every session |
| **Agent choice** | Agent decides to use | Agent must follow |
| **Example** | jira-openclaw | memory protocol |
