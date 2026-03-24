# Access Control

> Who can do what, and how permissions are managed.

## Permission Model

### Human Permissions

| Role | Can do |
|------|--------|
| **Owner** (Arturito) | Everything. Final authority on all decisions. |
| **Collaborator** | Read/write on assigned projects. Cannot change org settings or delete data. |
| **Viewer** | Read-only access to shared resources. |

### Agent Permissions

| Level | Can do | Examples |
|-------|--------|----------|
| **Read** | Access files, query databases, search knowledge | RAG retrieval, file listing |
| **Write** | Create files, update records, send messages | Code commits, knowledge embedding |
| **Execute** | Run code, trigger deployments, manage infrastructure | CI/CD, task execution |
| **Admin** | Change permissions, create agents, modify org settings | Only with human approval |

### The Principle of Least Privilege

Every agent starts with **Read** permissions. Additional permissions are granted per-project, per-task, and documented in the agent's profile.

No agent has permanent Admin access. Admin actions require human confirmation every time.

## Integration Permissions

| Integration | Agent access level | Notes |
|-------------|-------------------|-------|
| GitHub | Write (code), Read (issues) | Push to branches, not main directly |
| Google Drive | Read/Write per folder | Scoped to org folders only |
| Slack | Read/Send | Cannot delete messages |
| Gmail | Read / Draft | Send requires human approval |
| Fly.io | Deploy only | Via CI/CD, not direct access |
| Database | Read/Write | Scoped to org's data only |

## Access Review

- Review agent permissions at every sprint boundary
- Remove permissions that haven't been used in 30 days
- Log all permission changes in the audit trail
