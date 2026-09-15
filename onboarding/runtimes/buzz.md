# Runtime adapter — Buzz

> How Buzz points at 7Ei_OS + TARCO vault. Protocols live in `protocols/` — do not restate them here.

**Last updated:** 2026-09-15

- **Status:** Active (primary GitHub producer on the Mac mini). Not the only L0 path.
- **L0:** keep a checkout of `Arturito7ei/7Ei_OS`; `git pull` before work; start at `bootstrap/CATCH_UP.md`.
- **L1:** checkout `Arturito7ei/7Ei-MC_TARCO`. Write only `vault/Memory/agents/<buzz-slug>/` (`7man` `7rd` `7ops` `7dev` `7fin` `7mkt`). Slug must match the vault table.
- **GitHub:** this runtime is the default producer into org repos. Branch/PR per `standards/repo-conventions.md`. Channel-linked epic work: `skills/epic-to-pr/SKILL.md`.
- **L2:** Buzz core / `~/.buzz/` stays runtime-private. Do not copy it into 7Ei_OS.
- **Secrets:** harness env only (`skills/secret-hygiene/SKILL.md`). Never paste values into channels, PRs, or the vault.
