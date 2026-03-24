# Incident Response Protocol

> What to do when things break.

## Severity Levels

| Level | Definition | Response time |
|-------|-----------|---------------|
| **P0** | Production down. Users cannot use the service. | Immediate |
| **P1** | Major feature broken. Workaround exists. | Within 2 hours |
| **P2** | Minor feature broken. Low impact. | Next sprint |
| **P3** | Cosmetic or edge case. | Backlog |

## Response Steps

### 1. Detect
- Monitor deploy logs (GitHub Actions)
- Check backend health: `https://7ei-backend.fly.dev/health`
- Review runtime logs via Vercel/Fly.io dashboards

### 2. Assess
- What's broken?
- Who's affected?
- Is there a workaround?
- What changed recently? (Check last merge/deploy)

### 3. Communicate
- Notify Arturito (human) immediately for P0/P1
- Log the incident in lessons.md

### 4. Fix
- **Rollback first** if the fix isn't obvious
- Then diagnose root cause
- Use Opus model for debugging

### 5. Post-mortem
- What happened?
- Why did it happen?
- What prevented detection?
- What changes prevent recurrence?
- Add to lessons.md and promote to protocol if systemic
