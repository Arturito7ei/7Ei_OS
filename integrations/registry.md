# Integration Registry

> How to add new integrations to the 7Ei ecosystem.

## Adding a New Integration

1. **Evaluate** — Does it serve a real need? Is there an existing integration that covers it?
2. **Document** — Create `integrations/{name}.md` with capabilities, permissions, and rules
3. **Configure** — Set up MCP connector or API access
4. **Test** — Verify read/write operations work correctly
5. **Approve** — Human approval required for any integration that can write or delete data
6. **Update** — Add to the agent instance profiles that need access

## Integration Checklist

- [ ] Documentation file created in `integrations/`
- [ ] Permissions scoped to minimum required
- [ ] Error handling documented
- [ ] Rate limits noted
- [ ] Secrets stored properly (see `security/secrets-management.md`)
- [ ] Added to relevant agent instance profiles
- [ ] Tested with harmless read-only operation
