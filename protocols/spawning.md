# Spawning Protocol

How to create new agent instances from the Arturito7EiT template.

## The Template System

Every 7Ei agent inherits from the **Arturito7EiT** primordial template. The template provides shared DNA (protocols, principles, memory architecture). Each instance adds its own identity, skills, and personality.

```
Arturito7EiT (Template)
├── Arturito7EiClaude (Instance — Claude Code runtime)
├── Arturito7EiClaw   (Instance — OpenClaw + Telegram runtime)
├── Legal7EiClaude    (Instance — Legal specialist)
├── Tech7EiClaw       (Instance — Tech Lead on OpenClaw)
└── ... future instances
```

## Spawning Checklist

### Step 1: Define Identity

Create `agents/{instance}/AGENT.md`:

```markdown
# {AgentName}

## Identity
- **Name:** {Display name}
- **Role:** {Primary role in the organization}
- **Template:** Arturito7EiT
- **Runtime:** {Claude Code | OpenClaw | other}

## Capabilities
- {What this agent can do that others cannot}
- {Specific tools, APIs, or integrations available}

## Personality
- {Communication style}
- {Decision-making approach}
- {How they handle uncertainty}

## Skills
- {Skill domains from the skill library}

## Knowledge Scope
- **Projects:** {Which repos/projects this agent works on}
- **Integrations:** {MCP servers, APIs, external tools}

## Coordination
- **Reports to:** {Orchestrator or human}
- **Collaborates with:** {Other agent instances}
- **Communication:** {Channels — Git, Telegram, Jira, etc.}
```

### Step 2: Inherit Protocols

The new agent must read and acknowledge:
- [ ] All files in `7Ei_OS/protocols/`
- [ ] `7Ei_OS/architecture/agent-template.md` (the DNA)
- [ ] `7Ei_OS/standards/naming.md` (naming conventions)
- [ ] `7Ei_OS/protocols/governance.md` (what it can/cannot do)

### Step 3: Initialize Memory

Create the agent's memory structure:

```
agents/{instance}/
├── AGENT.md           # Identity (Tier 0)
└── config.yaml        # Runtime configuration

memory/
├── long-term.md       # Tier 1 — starts empty
├── recent.md          # Tier 2 — starts empty
└── project.md         # Tier 3 — starts with assigned projects

tasks/
├── todo.md            # Tier 3 — starts empty
└── lessons.md         # Tier 2 — starts empty
```

### Step 4: Assign Projects

- Add project entries to `memory/project.md` with repo URLs and roles
- Ensure each assigned repo has a `CLAUDE.md` referencing 7Ei_OS
- Grant the agent appropriate GitHub access

### Step 5: Verify

The new agent should be able to answer:

> "If I learn something new, which memory tier does it belong to and where do I store it?"

Test with 5 examples:
1. "I discovered the API uses OAuth 2.0" → Tier 2 (`recent.md`), promote to Tier 1 if stable
2. "The human corrected my commit message style" → Tier 2 (`lessons.md`)
3. "I prefer concise communication" → Tier 0 (`AGENT.md` personality)
4. "This project uses React 18" → Layer 3 (project `CLAUDE.md`)
5. "I'm currently blocked on API auth" → Tier 3 (`project.md`)

If all 5 are correct, the agent is operational.

## Runtime Configuration

```yaml
# agents/{instance}/config.yaml
agent_id: arturito7eiclaude
template: arturito7eit
runtime: claude-code
model: claude-opus-4-6

repos:
  - Arturito7ei/Open7Ei-MC
  - Arturito7ei/7Ei_OS
  - Arturito7ei/7EiBank
  - Arturito7ei/Arturito7ei

integrations:
  - github
  - jira
  - obsidian

memory_path: memory/
tasks_path: tasks/
```

## Governance

- **Spawning a new agent requires orchestrator approval** (Tier 2)
- **Modifying the template itself requires human approval** (Tier 3)
- Each new instance must be documented in the OS README's agent table
- New agents start with minimal permissions and earn trust through verified work
