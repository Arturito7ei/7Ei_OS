# Mission Control App

**Repo:** [Arturito7ei/7Ei-Mission_Control_App](https://github.com/Arturito7ei/7Ei-Mission_Control_App)
**Backend:** https://7ei-backend.fly.dev
**Status:** Paused since 2026-08-29. Do not start Sprint 4.

## What It Is

AI-powered virtual office in your pocket. Create an org, spin up AI agents (starting with Arturito as Chief of Staff), assign tasks, chat, manage knowledge. Mobile-first (React Native) + web (Next.js) + backend (Fastify on Fly.io).

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Node.js 22, TypeScript, Fastify, Drizzle ORM, Turso (libSQL) |
| Mobile | React Native (Expo SDK 51) |
| Web | Next.js 15 App Router, Vercel |
| Auth | Clerk |
| Vector | Pinecone |
| LLM | Anthropic / OpenAI / Gemini via llm-router.ts |
| CI/CD | GitHub Actions → Fly.io (auto-deploy on merge to main) |
| Tests | Node.js built-in test runner |

## Sprint History

| Sprint | What shipped | Tests | PR |
|--------|-------------|-------|----|
| Sprint 1 | Onboarding, org creation, Arturito auto-spawn, RAG, knowledge embed, agent proposal, per-org API keys | 86 pass, 2 fail | Merged |
| Sprint 2 | Test fixes, cost centre, multi-agent + Silver Board, skill library, budget alerts | 134 pass, 0 fail | PR #14 |
| Sprint 3 | Google Drive OAuth, Drive RAG bridge, knowledge upload, Knowledge tab, task execution, agent routing | 85 pass, 9 fail (Node v25) | PR #15 |

## Key Files

| File | Purpose |
|------|--------|
| CLAUDE.md | Technical requirements — Claude Code reads first |
| backend/src/routes/all.ts | All API routes |
| backend/src/services/agent-executor.ts | Core LLM execution loop |
| backend/src/services/llm-router.ts | Unified streaming across providers |
| backend/src/db/schema.ts | Drizzle ORM schema |

## Roadmap

Historical. Telegram, Gmail, and later Arturita Telegram work already landed in `7Ei-Mission_Control_App` (last commit 2026-08-29). Do not execute this list.

- Sprint 4: Communications hub (Telegram, Gmail) — already shipped in the app repo
- Sprint 5: Kanban board + Jira sync
- Sprint 6: Silver Board — call [Arturito7ei/silver-board](https://github.com/Arturito7ei/silver-board). Do not grow a second roster (`protocols/silver-board.md`)
- Sprint 7: Web desktop feature parity
- Sprint 8: Polish + App Store submission
