# Vercel Integration

**Team:** arturito-8100s-projects
**Agent access:** Read + Deploy (via Dispatch MCP)

## Capabilities

| Action | Permission |
|--------|----------|
| List projects | Read |
| List deployments | Read |
| Get build logs | Read |
| Get runtime logs | Read |
| Deploy | Write (via CI/CD) |
| Check domain availability | Read |

## Projects

[To be populated from Vercel project list]

## Rules

- Production deployments happen via GitHub Actions on merge to main
- Preview deployments are automatic on PR creation
- Never deploy directly — always go through CI/CD
