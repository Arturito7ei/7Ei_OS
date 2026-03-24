# Testing Standards

> How testing works across 7Ei projects.

## Rules

1. **Every new function gets a test** — no exceptions
2. **Tests run after every work order** — not just at the end
3. **Pre-existing failures are documented** — not ignored
4. **Tests are deterministic** — no flaky tests in main
5. **Test names describe behaviour** — `[TASK-ID] description of what is tested`

## Test Runner

- **Backend:** Node.js built-in test runner (`node --test`)
- **No external frameworks** — keep dependencies minimal

## Test Structure

```typescript
import { test } from 'node:test'
import assert from 'node:assert/strict'

test('[TASK-ID] description', async () => {
  // arrange
  // act
  // assert
  assert.strictEqual(actual, expected)
})
```

## What to Test

| Layer | What to test | Example |
|-------|-------------|--------|
| Routes | Input validation, response codes, auth | POST /api/orgs returns 201 |
| Services | Business logic, edge cases | buildSystemPrompt includes org context |
| Utilities | Pure functions | chunkText returns correct count |
| Integration | End-to-end flows | Create org → agent exists |

## Test Hygiene

- Clean up test data after each test
- Don't depend on test execution order
- Mock external services (Pinecone, LLM APIs)
- Keep tests fast — under 1 second each
