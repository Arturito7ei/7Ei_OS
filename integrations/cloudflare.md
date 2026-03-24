# Cloudflare Integration

**Account:** Active (via MCP)
**Agent access:** Read + limited Write (via Dispatch MCP)

## Services Available

| Service | Access | Use case |
|---------|--------|----------|
| Workers | Read/Deploy | Edge functions |
| D1 | Read/Write/Query | SQL databases at the edge |
| KV | Read/Write | Key-value storage |
| R2 | Read/Write | Object storage |
| Hyperdrive | Read/Configure | Database connection pooling |
| DNS | Read | Domain management |

## Rules

- Never delete production databases without human approval
- Never modify DNS records without human approval
- Workers deployments follow the same approval tiers as other deployments
