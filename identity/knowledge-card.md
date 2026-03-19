# Agent Knowledge Card

Every agent maintains a knowledge card — a manifest of what knowledge they hold and at which layer.

## Template

```yaml
agent: {agent-id}
updated: {date}

knowledge:
  layer_0_os:
    source: 7Ei_OS/protocols/
    status: inherited  # All agents inherit L0

  layer_1_org:
    - domain: company-identity
      source: platform/org/7ei.yaml
    - domain: shared-tools
      source: memory/long-term.md#org-facts
    - domain: coordination
      source: platform/coordination/

  layer_2_identity:
    - source: agents/{instance}/AGENT.md
    - source: agents/{instance}/config.yaml
    - source: memory/long-term.md#personal-patterns

  layer_3_projects:
    - project: 7eibank
      source: projects/7eibank/
      role: lead
    - project: open7ei-mc
      source: Arturito7ei/Open7Ei-MC
      role: developer

  layer_4_session:
    - source: memory/recent.md
    - source: memory/project.md
    - source: tasks/todo.md
    - source: tasks/lessons.md
```

## Purpose

- Makes explicit what each agent knows and doesn't know
- Prevents agents from acting on knowledge they don't have
- Enables the orchestrator to route tasks to the right agent
- Supports onboarding new agents (copy card, fill in L2-L3)
