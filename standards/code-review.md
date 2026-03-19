# Code Review Checklist

Universal review standards for all 7Ei repos. Apply these when reviewing PRs, before committing, or when self-reviewing work.

## Before Submitting

### Correctness
- [ ] Does the change do what it claims to do?
- [ ] Are edge cases handled?
- [ ] Are error states handled for all async operations?
- [ ] No hardcoded values that should be configurable

### Security
- [ ] No secrets, API keys, or credentials in code (check `.env`, `config`, hardcoded strings)
- [ ] No command injection, XSS, SQL injection, or OWASP top 10 vulnerabilities
- [ ] User input is validated at system boundaries
- [ ] Sensitive data is not logged

### Simplicity
- [ ] Is this the simplest solution that works?
- [ ] No premature abstractions — three similar lines is better than an unnecessary helper
- [ ] No features, refactoring, or "improvements" beyond what was asked
- [ ] No unnecessary error handling for scenarios that can't happen

### Readability
- [ ] Functions under 30 lines (split if longer)
- [ ] Logic duplicated more than twice is extracted
- [ ] Variable names describe what they hold, not how they're computed
- [ ] Comments only where the logic isn't self-evident — no noise comments

### Compatibility
- [ ] No backwards-compatibility hacks (renamed `_vars`, re-exports, `// removed` comments)
- [ ] If something is unused, delete it completely
- [ ] No TODO comments without a linked issue or task

### Testing
- [ ] Changes are tested (automated or manually verified)
- [ ] Tests pass locally before pushing
- [ ] New behavior has corresponding test coverage

## Review Process

### For the Author
1. Self-review against this checklist before requesting review
2. Write a clear PR description explaining **why**, not just **what**
3. Keep PRs focused — one concern per PR

### For the Reviewer
1. Run the checklist above
2. Check if the change aligns with the project's `CLAUDE.md` standards
3. Ask: "Would a staff engineer approve this?"
4. Approve, request changes, or escalate

### Auto-Approve Criteria
Trivial changes that can be merged without full review:
- Typo fixes in documentation
- Comment updates
- Dependency version bumps (patch level)
- Memory file updates (`memory/`, `tasks/`)

## Red Flags

Stop and investigate if you see:
- Changes to files the PR shouldn't need to touch
- New dependencies without justification
- Configuration changes without documentation
- Tests removed or disabled
- Force-push to shared branches
- `.env` or credential files staged for commit
