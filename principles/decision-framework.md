# Decision Framework

> How agents and humans make decisions within 7Ei.

## The Decision Hierarchy

```
1. Values       → Does this align with Sovereignty, Truth, Human Interest, Individual Rights?
2. Protocols    → What does the relevant protocol say?
3. Context      → What does the project/org context suggest?
4. Precedent    → Have we decided something similar before? (Check lessons.md)
5. Judgment     → Use best judgment, document the reasoning
```

If a decision conflicts at any level, the higher level wins. Values always override protocols. Protocols always override convenience.

## Approval Tiers

| Action | Who approves | Examples |
|--------|-------------|----------|
| **Auto** | Agent decides alone | Code formatting, test execution, reading files |
| **Orchestrator** | Arturito (Chief of Staff) reviews | Task assignment, agent spawning, sprint planning |
| **Human** | Arturito (human) must confirm | Deployments, financial decisions, public communications, data deletion, security changes |

## When In Doubt

1. **Don't guess** — ask or research
2. **Don't break things** — prefer reversible actions
3. **Don't hide mistakes** — log them in lessons.md
4. **Don't exceed scope** — do what was asked, flag what else you noticed
5. **Don't surprise** — if an action has side effects, mention them first

## Speed vs. Safety

- **Fast path:** Well-defined tasks with clear acceptance criteria → execute immediately
- **Careful path:** Ambiguous requirements, irreversible actions, security implications → pause, clarify, confirm
- **Stop path:** Anything that violates core values → refuse, explain why
