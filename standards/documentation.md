# Documentation Standards

> How docs should be written across 7Ei.

## General Rules

1. **Write for agents AND humans** — clear markdown that both can parse
2. **One idea per file** — no megadocs. Split by topic.
3. **Lead with the action** — what should the reader DO, not just know
4. **Include examples** — every protocol needs at least one concrete example
5. **Date everything** — last updated date on every document
6. **Link, don't duplicate** — reference other files instead of copying content

## File Naming

- Lowercase, hyphens: `sprint-cycle.md`, `access-control.md`
- No spaces, no underscores in filenames
- Descriptive names: `data-residency.md` not `dr.md`

## Structure

```markdown
# Title

> One-line summary of what this document covers.

## Section

Content...
```

- Use blockquote (`>`) for the one-line summary
- Use tables for structured data
- Use code blocks for commands, configs, and examples
- Use `**bold**` sparingly — for key terms only

## README Files

Every folder that isn't self-explanatory should have a README.md explaining:
- What's in this folder
- How to use the contents
- Where to start reading
