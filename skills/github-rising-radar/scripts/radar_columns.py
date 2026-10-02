"""Shared Description-column helpers for GitHub Rising Radar.

Scan, dashboard, and hub must all emit Description after Repo (and
before Why / metrics). Do not drop this column in a chat-only table.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_LINK = re.compile(r"\[([^\]]+)\]\(https?://github\.com/([^)\s]+)\)")
BARE_REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def fmt_desc(value: dict | str | None, limit: int = 140) -> str:
    """One-line markdown-safe description, or an em dash if missing."""
    raw = value.get("description") if isinstance(value, dict) else value
    text = " ".join((raw or "").split()).replace("|", "/")
    if not text:
        return "—"
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def repo_key_from_cell(cell: str) -> str | None:
    """Extract owner/name from a markdown Repo cell."""
    m = REPO_LINK.search(cell or "")
    if m:
        parts = m.group(2).strip().rstrip("/").split("/")
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"
    bare = (cell or "").strip()
    if BARE_REPO.fullmatch(bare):
        return bare
    return None


def insert_description_column(
    rows: list[list[str]],
    desc_by_repo: dict[str, str],
    *,
    limit: int = 140,
) -> list[list[str]]:
    """Insert Description immediately after Repo when the table lacks it.

    Leaves tables that already have a Description header untouched so
    curated verdict text is not overwritten by the GitHub blurb.
    """
    if not rows:
        return rows
    header = [c.strip() for c in rows[0]]
    lowered = [h.lower() for h in header]
    if "description" in lowered:
        return rows
    try:
        repo_idx = lowered.index("repo")
    except ValueError:
        return rows
    insert_at = repo_idx + 1
    out = [header[:insert_at] + ["Description"] + header[insert_at:]]
    for row in rows[1:]:
        padded = list(row) + [""] * max(0, len(header) - len(row))
        key = repo_key_from_cell(padded[repo_idx] if repo_idx < len(padded) else "")
        raw = desc_by_repo.get(key or "") if key else None
        desc = fmt_desc(raw, limit=limit)
        out.append(padded[:insert_at] + [desc] + padded[insert_at:])
    return out


def load_description_index(skill_root: Path) -> dict[str, str]:
    """owner/name → GitHub description from snapshots, latest wins."""
    index: dict[str, str] = {}
    data_dir = skill_root / "data"
    paths: list[Path] = []
    snap_dir = data_dir / "snapshots"
    if snap_dir.is_dir():
        paths.extend(sorted(snap_dir.glob("*.json")))
    latest = data_dir / "latest.json"
    if latest.exists():
        paths.append(latest)
    for path in paths:
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for repo in payload.get("repos", []):
            name = repo.get("full_name")
            desc = repo.get("description")
            if name and desc:
                index[name] = desc
    return index
