"""Curated Local models + Free model API catalogs for the research hub.

Scored 2026-10-12 by 7RD. Sources are nest RESEARCH notes (paths in
PAGE_SOURCES) plus vendor URLs fetched the same day. Cloud rows send
prompts off-box — Precedence 01. Adopt none of the free APIs as org-default.
"""

from __future__ import annotations

from typing import TypedDict


class CatalogItem(TypedDict):
    name: str
    url: str
    description: str
    verdict: str
    meta: str


PAGE_SOURCES = {
    "local-models": [
        "RESEARCH/SELF_HOSTED_UNFILTERED_LLM_EVAL_2026_09_16.md",
        "RESEARCH/MAC_MINI_OLLAMA_SCAN_2026_09_16.md",
        "RESEARCH/LLM_API_AND_LOCAL_OPTIONS_HERMES_2026_09_23.md",
        "https://github.com/ggml-org/llama.cpp",
        "https://ollama.com",
        "https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive",
    ],
    "free-apis": [
        "RESEARCH/FREE_LLM_APIS_CLASSIFIED_2026_10_12.md",
        "https://console.groq.com/docs/rate-limits",
        "https://ai.google.dev/gemini-api/docs/pricing",
        "https://openrouter.ai/api/v1/models",
        "https://developers.cloudflare.com/workers-ai/platform/pricing/",
    ],
}

SCORED = "2026-10-12"

LOCAL_RUNTIMES: list[CatalogItem] = [
    {
        "name": "llama.cpp",
        "url": "https://github.com/ggml-org/llama.cpp",
        "description": "Local GGUF server. TARCOH / Hermes Desktop already runs this on the Mac mini (OpenAI-compat :18434).",
        "verdict": "Adopt",
        "meta": "Self-hosted · MIT · no cloud",
    },
    {
        "name": "Ollama",
        "url": "https://ollama.com",
        "description": "Local OpenAI-compat runtime for Mission Control / Arturita. Already the 7Ei default for on-box tags.",
        "verdict": "Adopt",
        "meta": "Self-hosted · MIT · docs.ollama.com",
    },
    {
        "name": "Hugging Face Hub (weights)",
        "url": "https://huggingface.co/models",
        "description": "Download GGUF / MLX / safetensors to disk. Not a hosted inference API — weights stay local after pull.",
        "verdict": "Adopt",
        "meta": "BYOK download · do not use HF Inference Providers as “free”",
    },
    {
        "name": "mlx-lm",
        "url": "https://github.com/ml-explore/mlx-lm",
        "description": "Apple Silicon native runtime. Useful on M-class when we want MLX quants instead of GGUF.",
        "verdict": "Trial",
        "meta": "Self-hosted · MIT · M-series only",
    },
    {
        "name": "LM Studio",
        "url": "https://lmstudio.ai",
        "description": "Desktop GUI + local OpenAI-compat server. Same 16 GB ceiling as llama.cpp / Ollama — no extra headroom.",
        "verdict": "Hold",
        "meta": "Local GUI · closed app · skip if llama.cpp already loaded",
    },
]

LOCAL_MODELS: list[CatalogItem] = [
    {
        "name": "Qwen3.5-9B Uncensored (HauhauCS Q6_K)",
        "url": "https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive",
        "description": "TARCOH local fallback. 9B dense, 262k native ctx, GGUF Q6_K ~6.9 GB on disk / ~3.5 GB llama-server RSS on the M4 mini.",
        "verdict": "Adopt",
        "meta": "16 GB box · llama.cpp · Apache-2.0",
    },
    {
        "name": "llama3.2:3b",
        "url": "https://ollama.com/library/llama3.2",
        "description": "Command Center / Arturita pipeline primary. ~2 GB Q4 — the tag the browser path actually looks for.",
        "verdict": "Adopt",
        "meta": "Ollama · ~2 GB · pulled 2026-09-16",
    },
    {
        "name": "nomic-embed-text",
        "url": "https://ollama.com/library/nomic-embed-text",
        "description": "Local embeddings only (274 MB). Keep installed; it is not a chat model.",
        "verdict": "Adopt",
        "meta": "Ollama · embeddings",
    },
    {
        "name": "qwen2.5-coder:7b",
        "url": "https://ollama.com/library/qwen2.5-coder",
        "description": "Installed coder tag (~4.7 GB Q4). Fits, but do not load alongside the 9B Hermes server on 16 GB.",
        "verdict": "Hold",
        "meta": "Ollama · 7B · MAX_LOADED_MODELS=1",
    },
    {
        "name": "dolphin3-abliterated:8b",
        "url": "https://ollama.com/huihui_ai/dolphin3-abliterated:8b",
        "description": "Unfiltered Dolphin 3 / Llama 3.1 8B (~5 GB). Trial only if Hermes Desktop 9B is stopped.",
        "verdict": "Trial",
        "meta": "Ollama · ~5 GB · 7MAN 2026-09-16",
    },
    {
        "name": "Hermes-3-Llama-3.1-8B",
        "url": "https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B",
        "description": "Nous uncensored instruct + native function-calling. Prefer this over a random 8B when the job is tool-calling.",
        "verdict": "Trial",
        "meta": "HF / Ollama hermes3 · agent/tools",
    },
    {
        "name": "qwen3-abliterated:14b",
        "url": "https://ollama.com/huihui_ai/qwen3-abliterated",
        "description": "Stronger unfiltered Qwen3 (~9 GB Q4). Do not pull on the 16 GB mini while Buzz + Hermes are resident.",
        "verdict": "Avoid",
        "meta": "Ollama · ~9 GB · RAM contest",
    },
    {
        "name": "Qwen3.8-27B Uncensored",
        "url": "https://ollama.com/search?q=abliterated",
        "description": "Bleeding-edge 27B unfiltered. Hold until a 32 GB+ box and a refusal + coding smoke test.",
        "verdict": "Hold",
        "meta": "Needs 32 GB+ · not on this mini",
    },
]

FREE_APIS: list[CatalogItem] = [
    {
        "name": "Groq openai/gpt-oss-20b",
        "url": "https://console.groq.com/docs/models",
        "description": "Fastest standing free chat ID already in Hermes. ~1000 t/s listed. Keep local Qwen as fallback.",
        "verdict": "Trial",
        "meta": "131k ctx · 30 RPM · 1K RPD · 8K TPM · 200K TPD",
    },
    {
        "name": "Groq openai/gpt-oss-120b",
        "url": "https://console.groq.com/docs/models",
        "description": "Same free Groq bucket, harder reasoning (~500 t/s). Use when 20B stalls.",
        "verdict": "Trial",
        "meta": "131k ctx · same Groq free limits as 20b",
    },
    {
        "name": "Groq qwen/qwen3.8-27b",
        "url": "https://console.groq.com/docs/models",
        "description": "Qwen-family coding on Groq free. Preview ID; max out 16k.",
        "verdict": "Trial",
        "meta": "131k ctx · same Groq free limits",
    },
    {
        "name": "Cloudflare GLM-4.7-Flash",
        "url": "https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/",
        "description": "Workers AI text + tools. Only if a Cloudflare account already exists — not a Hermes primary.",
        "verdict": "Trial",
        "meta": "131k ctx · 10k Neurons/day · 300 RPM text",
    },
    {
        "name": "Cloudflare Gemma 4 26B A4B",
        "url": "https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/",
        "description": "Open multimodal on the same Cloudflare neuron budget.",
        "verdict": "Trial",
        "meta": "256k ctx · 10k Neurons/day",
    },
    {
        "name": "Gemini 3.8 Flash",
        "url": "https://ai.google.dev/gemini-api/docs/pricing",
        "description": "Long-horizon coding + agents, 1M context. Unpaid Gemini: Google may use prompts/responses to improve products.",
        "verdict": "Hold",
        "meta": "1M in / 64k out · P01 training-use · Arturito before real data",
    },
    {
        "name": "Gemini 3.6 Flash / 3.5 Flash-Lite / 3.1 Flash-Lite / 3 Flash",
        "url": "https://ai.google.dev/gemini-api/docs/models/gemini",
        "description": "Same unpaid Gemini contract as 3.8 Flash. Gemini 3.1 Pro has no free API tier.",
        "verdict": "Hold",
        "meta": "1M-class · RPM only in AI Studio",
    },
    {
        "name": "OpenRouter thinkingmachines/inkling:free",
        "url": "https://openrouter.ai/thinkingmachines/inkling:free",
        "description": "975B / 41B active MoE, 1M ctx, tools. Daily cap is shared across all OpenRouter :free models.",
        "verdict": "Hold",
        "meta": "20 RPM · 50 RPD until ≥$10 lifetime · else 1000 RPD",
    },
    {
        "name": "OpenRouter nemotron-3-ultra-550b:free",
        "url": "https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free",
        "description": "Frontier reason + orchestration (550B / 55B). Same shared :free bucket.",
        "verdict": "Hold",
        "meta": "1M ctx · shared OR free RPD",
    },
    {
        "name": "OpenRouter google/gemma-4-31b-it:free",
        "url": "https://openrouter.ai/google/gemma-4-31b-it:free",
        "description": "Open multimodal + thinking + tools on the :free pool.",
        "verdict": "Hold",
        "meta": "262k ctx · shared OR free RPD",
    },
    {
        "name": "OpenRouter cohere/north-mini-code:free",
        "url": "https://openrouter.ai/cohere/north-mini-code:free",
        "description": "Agentic coding MoE (30B / 3B). Same 50 RPD until paid credits.",
        "verdict": "Hold",
        "meta": "256k ctx · shared OR free RPD",
    },
    {
        "name": "SambaNova DeepSeek-V3.1 / gpt-oss-120b",
        "url": "https://cloud.sambanova.ai/plans",
        "description": "Frontier OSS on a tiny daily cap (20 RPD). Prefer Groq for gpt-oss-120b.",
        "verdict": "Hold",
        "meta": "20 RPM · 20 RPD · 200k TPD · no card",
    },
    {
        "name": "Cohere command-a-03-2025",
        "url": "https://docs.cohere.com/docs/command-a",
        "description": "Trial keys only: eval/RAG, not production. 1,000 calls/month.",
        "verdict": "Hold",
        "meta": "256k ctx · 20 RPM · production forbidden",
    },
]

NOT_FREE: list[CatalogItem] = [
    {
        "name": "Cerebras",
        "url": "https://inference-docs.cerebras.ai/support/rate-limits",
        "description": "Card + $5 / 30 days. FAQ: no permanently free tier.",
        "verdict": "Avoid",
        "meta": "Not standing free",
    },
    {
        "name": "Hugging Face Inference Providers",
        "url": "https://huggingface.co/docs/inference-providers/pricing",
        "description": "Free accounts: none monthly credits (changed ~7–12 Oct 2026). Hub downloads are still fine.",
        "verdict": "Avoid",
        "meta": "Pay-as-you-go inference",
    },
    {
        "name": "GitHub Models",
        "url": "https://docs.github.com/en/github-models",
        "description": "Fully retired 30 Jul 2026.",
        "verdict": "Avoid",
        "meta": "Gone",
    },
    {
        "name": "Together / Chutes / Fireworks",
        "url": "https://gravity.fast/data/free-llm-api-tiers/",
        "description": "No standing published free chat quota (Together min $5; Chutes FAQ: no free tier).",
        "verdict": "Avoid",
        "meta": "Not 100% free",
    },
]
