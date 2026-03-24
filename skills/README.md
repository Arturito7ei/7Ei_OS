# Skill System

> Skills are modular capabilities that agents can learn, use, and share.

## What Is a Skill?

A skill is a markdown file (SKILL.md) that teaches an agent how to perform a specific task. Skills are:

- **Composable** — skills can reference other skills
- **Assignable** — specific skills can be assigned to specific agents
- **Versionable** — skills evolve through git commits
- **Forkable** — copy and personalise a skill for your org

## Skill Structure

```
skills/
├── README.md              ← You are here
├── catalog.md             ← Master list of all skills
├── templates/
│   └── SKILL-TEMPLATE.md  ← Template for creating new skills
└── domains/
    ├── engineering/       ← Code review, debugging, testing
    ├── operations/        ← Process docs, runbooks, status reports
    ├── communication/     ← Email drafting, Slack messaging, meeting prep
    ├── knowledge/         ← Research, synthesis, documentation
    ├── project-mgmt/      ← Sprint planning, task breakdown, roadmaps
    └── integration/       ← Tool-specific skills (Jira, Drive, etc.)
```

## Skill Lifecycle

1. **Create** — write a SKILL.md following the template
2. **Test** — assign to an agent, run against real tasks
3. **Refine** — update based on performance
4. **Promote** — if universally useful, add to the shared library
5. **Archive** — if superseded, move to archive with reason

## Skill Library

**Source:** [Arturito7ei/skill-library](https://github.com/Arturito7ei/skill-library)

The skill library is synced to Mission Control via `POST /api/skills/sync`. Agents browse and self-assign skills through the Skill Library tab in the app.

## Creating a New Skill

See `templates/SKILL-TEMPLATE.md` for the required format.
