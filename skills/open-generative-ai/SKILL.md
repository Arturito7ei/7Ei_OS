---
name: open-generative-ai
description: "Drive Open Generative AI for marketing creatives (image, video, lip-sync, Marketing Studio) via hosted MuAPI, desktop, or self-host. Use for campaign visuals, ad variations, talking-head clips. Loop 7LEX before privacy/security claims."
---

# Open Generative AI

**Cluster:** Tools (Marketing / Growth)  
**Owner:** 7MKT  
**Upstream:** https://github.com/Anil-matcha/Open-Generative-AI  
**License:** MIT (verified via GitHub `license.spdx_id`, 2026-10-22)  
**Hosted UI:** https://muapi.ai/open-generative-ai  
**API gateway:** [Muapi.ai](https://muapi.ai) (cloud model routing)

## What it is

Open Generative AI is an open-source **image / video / audio / lip-sync / cinema / marketing** studio (Next.js + Electron). It fronts a large model catalog (README claims 400+ / 600+ across studios — treat counts as upstream marketing; verify in `packages/studio/src/models.js` before citing exact numbers publicly).

**Studios that matter for 7MKT**

| Studio | Job |
|---|---|
| **Image Studio** | Text-to-image and image-to-image (multi-ref up to ~14 on some models) |
| **Video Studio** | Text-to-video and image-to-video |
| **Marketing Studio** | Ad / marketing creative variations from a single input |
| **Lip Sync Studio** | Portrait or video + audio → talking / lipsync clips |
| **Cinema Studio** | Shot framing with camera / lens / aperture prompt controls |
| **Workflow Studio** | Node-based multi-step pipelines (also API-callable) |
| **Audio / Clipping / Vibe Motion / Agent / Design Agent** | Adjacent creative pipelines |

## Three run modes

| Mode | When | Sovereignty note |
|---|---|---|
| **Hosted** | Fastest — browser at muapi.ai/open-generative-ai | Prompts + media go through MuAPI cloud |
| **Desktop app** | Prebuilt macOS / Windows / Linux installers (v2.x releases) | UI local; cloud models still need MuAPI key unless Local toggle |
| **Self-host from source** | `git clone --recurse-submodules` → `npm run setup` → `npm run electron:dev` or `npm run dev` | Same BYOK pattern; local engines optional |

### Local inference (desktop only)

- **sd.cpp** (bundled) — SD 1.5 / SDXL / Z-Image on Metal (Apple Silicon) or CUDA/Vulkan/ROCm
- **Wan2GP** (BYO) — heavier image + video models; CUDA/ROCm host, optional remote MCP

Cloud path still needs a [Muapi access key](https://muapi.ai/access-keys). Store keys via 1Password / env — never paste into chat or vault notes (see `secret-hygiene`).

## When to use (7MKT)

- Draft **campaign stills**, hero images, product mock visuals for OUTBOX review
- Generate **ad variations** (Marketing Studio) before human brand pass
- Produce **short video / lipsync** drafts paired with Chatterbox TTS voice clones
- Prototype **multi-step creatives** in Workflow Studio before handoff to 7DEV for productized pipelines
- Explore model options for a brief without locking 7Ei to one closed SaaS UI

## When not to use

- **Public publish** of assets that imply privacy, security, compliance, or data-handling claims — loop **7LEX** first
- Treating vendor **"no content filters"** marketing as a 7Ei policy — Precedence 01–03 and brand voice still bind outward copy and creatives
- Citing **ship dates, model counts, or competitor pricing** from the upstream README without re-checking primary sources
- Assuming **self-host = offline** — most flagship models (Kling, Sora, Veo, Midjourney-class, etc.) are MuAPI-routed unless Local engines cover them

## Agent workflow

1. **Brief** — audience, venture, one claim, aspect ratio, still vs motion, brand constraints
2. **Mode** — prefer desktop Local for sensitive drafts when models allow; else hosted/desktop + MuAPI BYOK
3. **Generate** — start in Marketing Studio or Image/Video Studio; keep prompts + seed/model IDs in the work log
4. **Brand pass** — match approved voice/visuals; discard overclaims and dark-pattern framing
5. **Route** — put external-ready drafts in `~/.buzz/OUTBOX/` until Thierry or 7MAN approves; do not publish from chat alone
6. **Escalate** — 7LEX for compliance-sensitive creatives; 7OPS if any security disclosure imagery/copy

## Quick start (operator)

```bash
# Option A — hosted (no install)
open "https://muapi.ai/open-generative-ai"

# Option B — desktop: download from GitHub Releases (v2.0.0+)
# macOS Gatekeeper: xattr -cr "/Applications/Open Generative AI.app" then Open

# Option C — from source
git clone --recurse-submodules https://github.com/Anil-matcha/Open-Generative-AI.git
cd Open-Generative-AI
npm run setup
npm run electron:dev   # or: npm run dev
```

## Related 7Ei skills

- [[TTS-Chatterbox]] — local voice clone for lipsync audio
- [[Video-Frames]] — extract frames/clips from generated video
- [[Meme-Maker]] — lightweight meme templates (not a substitute for this studio)
- [[Diagram-Maker]] — architecture/explainer diagrams (not photoreal marketing)

## Sources

- Upstream README: https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md
- Repo metadata: `gh api repos/Anil-matcha/Open-Generative-AI` (MIT, pushed_at 2026-10-21)
- Departments cluster ownership: vault `Company/Departments.md` — Tools → 7MKT

## Verdict (marketing ops)

**Trial** for internal creative production and OUTBOX drafts. Not a sovereignty-complete stack for Precedence 01 workloads unless restricted to Local engines and verified offline models. Do not echo upstream "unrestricted / no filters" language in 7Ei public messaging.
