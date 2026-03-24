# Sprint Cycle Protocol

> The repeatable loop for shipping software at 7Ei.

## The Cycle

```
1. PLAN    → Arturito says "next sprint"
           → Dispatch reads repo, produces execution plan
           → Push plan to 7Ei_OS/projects/{project}/sprints/
           → Create GitHub Issues

2. EXECUTE → Claude Code reads the execution plan
           → Implements work orders sequentially
           → Runs tests after each work order
           → Commits and pushes to feature branch

3. MERGE   → Dispatch creates PR with summary
           → Dispatch merges to main
           → GitHub Actions auto-deploys

4. UPDATE  → Dispatch updates CLAUDE.md in the project repo
           → Dispatch closes GitHub Issues
           → Dispatch updates sprint history in 7Ei_OS
           → Dispatch writes lessons to lessons.md

5. TEST    → Dispatch prompts Arturito to test
           → Arturito tests from phone
           → Feedback goes back to step 1
```

## Model Selection

| Task type | Model | Why |
|-----------|-------|-----|
| Well-defined specs, exact file paths | Sonnet | Faster, cheaper, follows instructions precisely |
| Diagnostic work, test failures | Opus | Better reasoning, finds root causes |
| Architectural decisions, ambiguity | Opus | Better judgment on trade-offs |
| UI implementation, CRUD endpoints | Sonnet | Pattern-following, efficient |

## Sprint Duration

- **Target:** 2 weeks
- **Work orders per sprint:** 4-6
- **Tests per sprint:** 20-40 new tests
- **Always:** Ship something real. No planning-only sprints.

## Post-Sprint Checklist

- [ ] All work orders complete
- [ ] Tests pass (document any pre-existing failures)
- [ ] PR merged to main
- [ ] Auto-deploy triggered and succeeded
- [ ] CLAUDE.md updated in project repo
- [ ] GitHub Issues created and closed
- [ ] Sprint archived in 7Ei_OS
- [ ] Lessons captured
- [ ] Arturito prompted to test
