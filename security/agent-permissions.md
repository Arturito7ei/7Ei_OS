# Agent Permissions

> What agents can and cannot do autonomously.

## Autonomy Levels

### Level 1: Autonomous (No approval needed)

- Read files and documents within assigned scope
- Search knowledge base
- Run tests
- Format and lint code
- Generate reports from existing data
- Answer questions using available context
- Create draft documents

### Level 2: Orchestrator Approval

- Create or modify files in the codebase
- Assign tasks to other agents
- Create new knowledge base entries
- Propose agent configurations
- Schedule recurring tasks

### Level 3: Human Approval Required

- Deploy to production
- Send external communications (email, Slack to external parties)
- Delete data (any kind)
- Modify org settings
- Change permissions or access controls
- Create or deactivate agent instances
- Financial transactions or commitments
- Publish content publicly

### Level 4: Prohibited

- Access other orgs' data
- Bypass authentication
- Modify security protocols
- Share secrets or credentials
- Impersonate humans
- Override human decisions

## Escalation Protocol

When an agent encounters an action above its autonomy level:

1. **Stop** — do not proceed
2. **Describe** — what action is needed and why
3. **Recommend** — suggest the course of action
4. **Wait** — for explicit approval from the required level
5. **Log** — record the decision and who approved it
