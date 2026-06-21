---
name: kronos
description: "Forecast financial candlesticks (OHLCV) with Kronos foundation model from NeoQuasar/HuggingFace."
---

# Kronos — Financial K-Line Foundation Model

Kronos is the first open-source foundation model for financial candlestick (K-line) sequences. Trained on 45+ global exchanges. Accepted at AAAI 2026.

## Models Available

| Model | Tokenizer | Context | Params | Open Source |
|---|---|---|---|---|
| Kronos-mini | Kronos-Tokenizer-2k | 2048 | 4.1M | ✅ |
| Kronos-small | Kronos-Tokenizer-base | 512 | 24.7M | ✅ |
| Kronos-base | Kronos-Tokenizer-base | 512 | 102.3M | ✅ |
| Kronos-large | Kronos-Tokenizer-base | 512 | 499.2M | ❌ |

**HuggingFace:** `NeoQuasar/Kronos-small`, `NeoQuasar/Kronos-base`, `NeoQuasar/Kronos-mini`

## Installation

```bash
pip install -r requirements.txt  # from the Kronos repo
# Core deps: torch, transformers, pandas, numpy
```

## Basic Forecasting

```python
from model import Kronos, KronosTokenizer, KronosPredictor

# Load model + tokenizer
tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-small")

predictor = KronosPredictor(model, tokenizer, max_context=512)

# Prepare OHLCV data (DataFrame with ['open','high','low','close', 'volume', 'amount'])
# x_timestamp = historical timestamps, y_timestamp = future timestamps to predict
pred_df = predictor.predict(
    df=x_df,
    x_timestamp=x_timestamp,
    y_timestamp=y_timestamp,
    pred_len=120,      # number of periods to forecast
    T=1.0,             # temperature
    top_p=0.9,         # nucleus sampling
    sample_count=1     # paths to average
)
```

## Key Constraints

- `max_context=512` for small/base models — lookback should not exceed 512
- Input DataFrame **must** have: `['open', 'high', 'low', 'close']`
- `volume` and `amount` are optional
- For batch prediction: all series must have the **same lookback and pred_len**

## Fine-Tuning

Uses Qlib for data prep + torchrun for multi-GPU training. See `finetune/` directory in repo.

## Live Demo

https://shiyu-coder.github.io/Kronos-demo/

## Paper

https://arxiv.org/abs/2508.02739

## Repo

https://github.com/shiyu-coder/Kronos
