---
name: reverse-engineer-anything
description: Inspect authorized local shipped artifacts with REA (JavaScript/Electron, .NET, Go metadata; native only after an operator-approved engine). Use when a claim depends on a binary or package rather than source. Refuse unauthorized, DRM, exploit, or pentest work.
---

# Reverse Engineer Anything (REA)

Inspect a **local, authorized** shipped artifact and explain a feature with Evidence — then rebuild a 7Ei version if asked. Analysis stays on-box. Do not use this skill for ordinary source-repo work; use `investigate` / repo tools instead.

**Cluster:** Engineering  
**Owner:** 7DEV (Accountable: 7MAN)  
**Upstream:** [morluto/rea](https://github.com/morluto/rea) · npm `rea-agents@6.4.0` · MIT  
**Official skill:** [`.agents/skills/reverse-engineer-anything/SKILL.md`](https://github.com/morluto/rea/blob/main/.agents/skills/reverse-engineer-anything/SKILL.md) (upstream v40)  
**Pairs with:** `secret-hygiene`, `gstack-openclaw-investigate`  
**Sovereignty:** Local CLI/MCP. Findings still leave the box if the agent model is cloud — summarize, do not dump.

## When to Use

- A claim depends on a **shipped** binary, ASAR, Electron app, `.app`, `.dll`, APK, or package — source is missing or untrusted
- Operator asks to understand a feature in an app 7Ei owns or is authorized to examine
- Compare two authorized versions of the same artifact
- Reconstruct a behavior for a 7Ei product after Evidence is in hand

**Do not use** when the repo source already answers the question, or when the request is pentest, CTF-flag, exploit, DRM bypass, cheat, or unauthorized access.

## Hard Gates (stop here)

1. **Authorization** — Target must be software 7Ei owns, Thierry authorized in this thread, or otherwise lawfully in scope ([REA DISCLAIMER](https://github.com/morluto/rea/blob/main/DISCLAIMER.md)). Public availability or "I have the file" is not permission. If authorization is unclear, stop and ask Thierry.
2. **No offensive work** — Refuse DRM/license circumvention, anti-cheat tampers, auth/bot bypass, exploit/PoC/payload writing, credential theft, unauthorized device ADB, live traffic intercept on others' systems. Offer owned-software interoperability or a 7Ei rebuild instead.
3. **Precedence 01** — REA does not upload the app. The **agent model** still sees tool output. Prefer `--json` to a local file, then a summary view. Never paste secrets, tokens, or full Evidence dumps into Buzz. Follow `secret-hygiene`.
4. **No silent setup** — Do not run `rea setup` / `npx rea-agents setup` except `--dry-run`. MCP bind and Hopper install are operator Desktop actions.
5. **No cracked tools** — Hopper, IDA, JEB, Ghidra only if legally installed by the operator. This host had **no** Hopper/Ghidra/IDA when scored 2026-10-13.

## Host facts (re-probe before citing)

Recorded 2026-10-13 on this Mac:

| Fact | Evidence |
|---|---|
| Node | `v22.23.1` (`node -v`) — meets REA `22.x >= 22.19` |
| Package | `npm view rea-agents version` → **6.4.0**, MIT |
| Global `rea` | **not on PATH** — use `npx -y rea-agents@6.4.0` |
| Native engines | Hopper / Ghidra / IDA **absent** |

If any row is stale, re-run the command. Do not quote an entitlement older than this session.

## Inputs

| Input | Required |
|---|---|
| Absolute local path (or already-open user-owned page/process the operator named) | Yes |
| Specific question (one feature / one behavior) | Yes |
| Authorization basis (own / Thierry said so / named contract) | Yes |
| Native provider (`ghidra` / `hopper` / `ida`) | Only if native decompile is in scope **and** `npx -y rea-agents@6.4.0 providers --json` lists it |

If the operator says only "my app" with no path or name, ask once. Do not pick an example app.

## Route the target

Use the **CLI** until MCP is bound. Pin the version you probed.

```bash
npx -y rea-agents@6.4.0 <command> /absolute/path --json
```

| Target | First command | Engine? |
|---|---|---|
| Extracted JS / Electron dir or `.asar` | `analyze-javascript-application PATH --json` | No |
| Large JS graph | same, then save JSON and `inspect-analysis-view` with `detail: "summary"` | No |
| .NET PE/CLI assembly | `inspect-managed-artifact` then `inspect-managed-members` | No |
| Go binary metadata | `inspect-go-binary PATH --json` | No |
| SQLite snapshot | `inspect-sqlite-database PATH --json` | No (Node 24.15+/26+ for native SQLite limits) |
| Mach-O / plist / signature (static) | `inspect-macho` / `inspect-plist` / `inspect-signature` | No Hopper |
| Native exe / `.app` / library | **Stop** unless a provider is installed; then `analyze PATH --provider <id> --json` | Hopper/Ghidra/IDA |
| APK (7Ei-owned) | `inspect-android-package` — JADX + JDK required | Extra tools |
| Source repo | **Do not use REA** — use `investigate` | — |

Default CLI format is TOON; always pass `--json` for agents. Evidence for a real Electron app can be hundreds of MB — write to a file, then project a summary. See [CLI and Evidence](https://github.com/morluto/rea/blob/main/docs/cli.md).

**Out of default 7Ei scope** (need an explicit per-target yes from Thierry): firmware extract, ADB device mutation, live packet capture, EVM chain work, attaching to someone else's running app, installing packages onto a phone.

## Workflow

1. **Authorize + identify.** Path, question, authorization line. Refuse if any gate fails.
2. **Smallest overview.** Run the first-command for that target. Save JSON under `.scratch/rea/` (disposable) or a named RESEARCH file if the operator wants a keepable record.
3. **Page, don't dump.** `inspect-analysis-view` / `jq` a summary. Trace one feature. Do not repeat an identical call.
4. **Ledger.** Every conclusion is observation, inference, or unknown — with Evidence IDs or file:offset citations. Static analysis is not runtime.
5. **Runtime only if static cannot answer** and the operator authorized execution of *this* target. Launched processes inherit the user account.
6. **Rebuild separately.** If asked to implement, write 7Ei code from the explained behavior. Do not copy proprietary assets or protected code.
7. **Redact.** Strings that look like keys → `secret-hygiene`. No raw env, tokens, or cookie jars in Buzz.

## Operator setup (human)

MCP + official skill install is **not** this skill. When Thierry wants Cursor wired:

```bash
npx rea-agents@6.4.0 setup --client cursor --dry-run --json
```

Review paths and backups. Apply only after he approves. Prefer `--skill=false` (this file is the 7Ei skill). Never `--all-detected` or `--install-hopper` unless he asked. Restart Cursor after a real apply. Docs: [installation.md](https://github.com/morluto/rea/blob/main/docs/installation.md).

Readiness (read-only): `npx -y rea-agents@6.4.0 doctor --json`.

## Output

Plain-language answer plus:

- Target path + SHA-256 / identity if REA returned it
- What was observed vs inferred vs unknown
- Commands actually run (version-pinned)
- What was **not** analyzed (no native engine, scope cut, authorization)

Never produce: exploit steps, DRM bypass, full decompiled dumps in channel, secret values.

## Quality Checklist

- [ ] Authorization stated
- [ ] Used REA only because source was insufficient
- [ ] Version-pinned CLI (`@6.4.0` or the live `npm view` result)
- [ ] Summary-first; no megabyte paste
- [ ] Observations ≠ inferences
- [ ] Secrets redacted
- [ ] Did not run `setup` except dry-run
- [ ] Rebuild (if any) is 7Ei-original

## Examples

**In scope**

> Look at `/Applications/OurApp.app` (7Ei build) and explain how export works. Show modules and Evidence, then sketch a 7Ei implementation.

**Out of scope**

> Crack this license check / dump this DRM'd game / write a PoC for the overflow / ADB into a customer's phone.

## Known Limitations

- This skill is **Trial**, not Adopt. MCP is unbound until operator setup.
- Native decompile needs a legal Hopper, Ghidra, or IDA install — none on this host as of 2026-10-13.
- Official skill on `main` may describe tools older npm releases lack. Trust `rea --help` / connected MCP `tools/list`.
- REA results can be wrong or incomplete. Verify before shipping.
- Cloud models see whatever you feed them. Local analysis ≠ local LLM.

## Escalation

| Situation | Who |
|---|---|
| Authorization / IP / third-party ToS | 7LEX → Thierry |
| User-data in Evidence | Thierry immediately (bypass queue) |
| MCP / Desktop bind / Hopper spend | Thierry |
| Secret in a binary string | 7OPS (names only) |
| Native engine missing | Stop; report — do not install |

## Attribution

Workflow adapted from [morluto/rea](https://github.com/morluto/rea) (MIT) official skill `reverse-engineer-anything` v40. Rewritten for 7Ei RACI, Precedence 01, and `secret-hygiene` — not a verbatim import. Vendor disclaimer remains binding: https://github.com/morluto/rea/blob/main/DISCLAIMER.md
