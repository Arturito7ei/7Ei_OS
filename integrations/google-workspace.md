# Google Workspace Integration

How 7Ei agents interact with Google Workspace tools — Docs, Sheets, Drive, Gmail, and Calendar.

## Services

| Service | Use For | Access Method |
|---------|---------|---------------|
| **Google Docs** | Long-form documents, proposals, reports | MCP or browser |
| **Google Sheets** | Data tables, budgets, tracking spreadsheets | MCP or browser |
| **Google Drive** | File storage, shared folders, document management | MCP or browser |
| **Gmail** | Email communications (Tier 3 approval required) | MCP or browser |
| **Google Calendar** | Scheduling, deadlines, recurring events | MCP or browser |

## Access Methods

### MCP (Google Workspace MCP Server)
Agents with MCP configuration can access Google Workspace programmatically:
- Read, create, and update Docs and Sheets
- Search and manage Drive files
- Read email (sending requires human approval)
- Query calendar events

### Browser-Based
Agents with browser access (e.g., Arturito7EiClaw) can use Google Workspace web apps directly.

### API
For CI/CD or headless automation, use Google Workspace APIs with service account credentials.

## Governance

| Action | Approval Tier |
|--------|--------------|
| Read documents and sheets | Auto-approved |
| Create/update internal documents | Auto-approved |
| Read email | Auto-approved |
| Send email | Human approval required |
| Share documents externally | Human approval required |
| Delete files | Human approval required |
| Access financial spreadsheets | Orchestrator approval |

## Document Conventions

### Naming
- Docs: `[Project] Document Title — YYYY-MM`
- Sheets: `[Project] Sheet Purpose — YYYY-MM`
- Folders: organized by project/department

### Ownership
- All documents owned by `arturito@7ei.ai`
- Agents create documents on behalf of the organization
- Documents inherit the project's access level (private by default)

## Integration with Agent Memory

Google Workspace content is Layer 1 (organizational) or Layer 3 (project) knowledge:
- Reference documents by their Google Drive URL in memory files
- Do not copy entire document contents into agent memory — link to them
- For key decisions in documents, extract the decision to the appropriate memory tier

## Security Rules

1. Never share documents with external parties without human approval
2. Never send emails without human approval
3. Store API credentials in `.env` only — never in code
4. Financial data requires orchestrator approval to access
5. Calendar invites to external parties require human approval
