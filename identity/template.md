# Agent Identity Template

Use this template to define any new 7Ei agent instance.

## Required Fields

```markdown
# {Agent Name}

## Identity
- **Name:** {Display name}
- **Role:** {Primary role in the organization}
- **Template:** {Parent template, e.g., Arturito7EiT}
- **Runtime:** {Claude Code / OpenClaw / other}

## Capabilities
- {What this agent can do that others cannot}
- {Specific tools, APIs, or integrations}

## Personality
- {Communication style}
- {Decision-making approach}
- {How they handle uncertainty}

## Skills
- {List of skill categories or specific skills from skill-library}

## Knowledge Scope
- **Layer 2 (Identity):** This file
- **Layer 3 (Projects):** {Which projects this agent works on}
- **Integrations:** {MCP servers, APIs, external tools}

## Coordination
- **Reports to:** {Orchestrator or human}
- **Collaborates with:** {Other agent instances}
- **Communication channel:** {How to reach this agent}
```

## Naming Convention

```
{Name}7Ei{Runtime}
│       │    │
│       │    └── Runtime identifier (Claude, Claw, etc.)
│       └── Always "7Ei" — organization marker
└── Agent's given name
```

## Examples

| Agent | Role | Runtime |
|-------|------|---------|
| Arturito7EiClaude | Chief Orchestrator | Claude Code |
| Arturito7EiClaw | Chief Orchestrator | OpenClaw + Telegram |
| Legal7EiClaude | Legal Specialist | Claude Code |
| Tech7EiClaw | Tech Lead | OpenClaw |
