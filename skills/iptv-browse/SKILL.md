---
name: iptv-browse
description: "Browse, search, and filter IPTV channels from iptv-org. Run sync to refresh channel data from GitHub."
metadata:
  homepage: https://github.com/iptv-org/iptv
allowed-tools:
  - exec
  - read
---

# IPTV Browse

Browse, search, and filter ~11,500 publicly available IPTV channels from the [iptv-org](https://github.com/iptv-org/iptv) repository. Includes a web dashboard and REST API.

## Quick Start

```bash
# 1. Sync channel data (first time or refresh)
python3 skills/iptv-browse/scripts/sync.py

# 2. Start the API + dashboard
python3 skills/iptv-browse/scripts/api.py --port 8080

# 3. Open dashboard
open http://localhost:8080/dashboard/
```

## Components

| File | Purpose |
|------|---------|
| `scripts/sync.py` | Fetch M3U from GitHub, parse to JSON |
| `scripts/query.py` | CLI search/filter/export |
| `scripts/api.py` | REST API server (FastAPI) |
| `scripts/api_start.sh` | Launcher script |
| `static/index.html` | Web dashboard |
| `data/iptv_channels.json` | Parsed channel data (~11.5k entries) |
| `data/sync_meta.json` | Last sync timestamp |

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /channels` | List channels (params: `q`, `country`, `category`, `limit`, `offset`) |
| `GET /channels/random` | Random picks (params: `n`, `country`, `category`) |
| `GET /channels/{name}` | Get one channel by name |
| `GET /stream/{name}` | Get stream URL for a channel |
| `GET /stats` | Stats overview |
| `GET /countries` | All countries with channel counts |
| `GET /categories` | All categories with channel counts |
| `GET /m3u/{country}` | Download filtered M3U playlist |
| `GET /dashboard/` | Web dashboard (HTML) |

## Dashboard Features

- 📱 Mobile-first responsive grid of channel cards
- 🔍 Text search + country + category filters
- ⭐ Favorites (localStorage)
- ▶️ HLS stream playback via hls.js
- 🔗 Open in external player
- 🌐 176 countries, 164 categories, 11,538 channels

## CLI Query Commands

```bash
python3 skills/iptv-browse/scripts/query.py search "BBC"
python3 skills/iptv-browse/scripts/query.py by-country CH
python3 skills/iptv-browse/scripts/query.py by-category News
python3 skills/iptv-browse/scripts/query.py random 10
python3 skills/iptv-browse/scripts/query.py stats
python3 skills/iptv-browse/scripts/query.py countries
python3 skills/iptv-browse/scripts/query.py categories
python3 skills/iptv-browse/scripts/query.py export my.json --country FR --category Music
```

## Notes

- Stream URLs are external; no files stored locally
- Data auto-expires after 7 days (re-run `sync.py` to refresh)
- API + dashboard must run on the same machine (Mac Mini)
- For remote access → Phase 4: Cloudflare Tunnel or ngrok
