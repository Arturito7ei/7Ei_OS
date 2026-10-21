#!/usr/bin/env python3
"""
sync_vault.py — Generate Obsidian Skill Library from catalog.md

Run this whenever catalog.md changes to regenerate the Obsidian vault.

Usage:
    python3 sync_vault.py [--dry-run]

Catalog is the SINGLE SOURCE OF TRUTH. The Obsidian vault is derived.

The script:
1. Parses skills/catalog.md to get all skills
2. Generates Obsidian notes for each skill in Skill-Library/<Category>/
3. Generates Skill-Library/Skill-Library.md (MOC)
4. Creates symlinks in workspace_skills/ for local access
"""

import os
import re
import sys
import argparse
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent.resolve()
SKILLS_DIR = REPO_ROOT / "skills"
CATALOG_PATH = SKILLS_DIR / "catalog.md"

# ── Paths ───────────────────────────────────────────────────────────────────
# Canonical 7Ei_OS install (override with SEIOS_ROOT env var)
SEIOS_ROOT = Path(os.environ.get(
    "7EIOS_ROOT",
    str(REPO_ROOT)  # assume 7Ei_OS is cloned here
))

# Obsidian vault (override with OBSIDIAN_VAULT env var)
OBSIDIAN_VAULT = Path(os.environ.get(
    "OBSIDIAN_VAULT",
    "/Users/artutito/Library/Mobile Documents/com~apple~CloudDocs/7Ei-MC_TARCO_Vault/TARCO-MC_Vault"
))
SKILL_LIBRARY_DIR = OBSIDIAN_VAULT / "Skill-Library"

# Workspace skills dir (override with WORKSPACE_SKILLS env var)
WORKSPACE_SKILLS = Path(os.environ.get(
    "WORKSPACE_SKILLS",
    "/Users/artutito/.openclaw/workspace/skills"
))

# ── Category emoji map ────────────────────────────────────────────────────────

CATEGORY_EMOJI = {
    "Finance": "📊",
    "Strategy": "🎯",
    "Engineering": "⚙️",
    "Operations": "🔄",
    "IT": "💻",
    "Communication": "📢",
    "Project Management": "📋",
    "Research": "🔬",
    "Integrations": "🌐",
    "Tools": "🛠️",
    "7Ei-Specific": "🚀",
}

# ── Parsing ──────────────────────────────────────────────────────────────────

VALID_CATEGORIES = set(CATEGORY_EMOJI.keys())

def parse_catalog(path: Path) -> list[dict]:
    """Parse catalog.md and return list of skill entries."""
    text = path.read_text()
    skills = []

    lines = text.split("\n")
    current_category = None

    for line in lines:
        # Category headers: ## 📊 Finance
        cat_match = re.match(r"^##?\s+([^\n]+)$", line.strip())
        if cat_match and not line.startswith("|"):
            raw = cat_match.group(1).strip()
            # Remove emoji prefix
            name = re.sub(r"^[^\w\s]+\s*", "", raw).strip()
            # Only treat as category if it's a known skill category
            current_category = name if name in VALID_CATEGORIES else None
            continue

        # Table rows:
        #   | Skill | Source | Description |                     (3 cols)
        #   | Skill | Source | Skill File | Description |        (4 cols — current catalog)
        if line.startswith("|") and "---" not in line and current_category:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 3 and parts[0] and parts[0] != "Skill":
                name, source = parts[0], parts[1]
                if len(parts) >= 4:
                    # Prefer explicit skill-file column when present; description is last
                    skill_file_hint, description = parts[2], parts[3]
                else:
                    skill_file_hint, description = "", parts[2]
                if name and description and not name.startswith("-"):
                    skill_dir = SKILLS_DIR / _slugify(name)
                    skill_file = skill_dir / "SKILL.md"
                    # If catalog points at a repo-relative skills/... path that exists, honor it
                    # (e.g. kepano nested paths stay as slugify dirs unless file missing elsewhere).
                    if skill_file_hint.startswith("`") and skill_file_hint.endswith("`"):
                        skill_file_hint = skill_file_hint.strip("`")
                    if skill_file_hint.startswith("skills/") and (REPO_ROOT / skill_file_hint).exists():
                        skill_file = REPO_ROOT / skill_file_hint
                    skills.append({
                        "name": name,
                        "source": source,
                        "description": description,
                        "category": current_category,
                        "skill_file": skill_file,
                        "slug": _slugify(name),
                    })

    return skills


def _slugify(name: str) -> str:
    """Convert 'CEO-Review' → 'ceo-review'."""
    return re.sub(r"[^\w]+", "-", name.lower()).strip("-")


# ── Obsidian note generation ────────────────────────────────────────────────

def generate_obsidian_note(skill: dict) -> str:
    """Generate Obsidian markdown for a single skill."""
    from datetime import date

    skill_file = skill["skill_file"]
    if skill_file.exists():
        try:
            rel_path = str(skill_file.relative_to(REPO_ROOT))
        except ValueError:
            rel_path = str(skill_file)
    else:
        rel_path = None

    # Read the actual SKILL.md for trigger info if available
    trigger = ""
    if skill_file.exists():
        content = skill_file.read_text()
        # Prefer YAML description frontmatter
        fm = re.search(r"(?m)^description:\s*[\"']?(.+?)[\"']?\s*$", content)
        if fm:
            trigger = fm.group(1).strip()
        else:
            m = re.search(
                r"(?is)##\s*(?:When to Use|Trigger)\s*\n+(.+?)(?:\n##\s|\Z)",
                content,
            )
            if m:
                # First non-empty bullet or line
                for line in m.group(1).splitlines():
                    line = line.strip().lstrip("-* ").strip()
                    if line:
                        trigger = line
                        break

    today = date.today().isoformat()
    path_display = rel_path or "(missing — add SKILL.md under 7Ei_OS/skills/)"

    return f"""---
title: "Skill: {skill['name']}"
created: 2026-06-22
updated: {today}
tags: [skill, {skill['category'].lower().replace(' ', '-')}]
status: active
---

# {skill['name']}

**Category:** {skill['category']}  
**Source:** {skill['source']}

{skill['description']}

## Skill File
`{path_display}` (in 7Ei_OS — git `Arturito7ei/7Ei_OS`)

## Trigger
> "{trigger or skill['description'][:120]}"

## More Info
See `{path_display}` in 7Ei_OS for full documentation.

---
⬆ Registry: [[Skill-Library]] · Map: [[MOC-Skills]] · Procedures: [[MOC-Protocols]]
"""

def generate_moc(skills: list[dict]) -> str:
    """Generate the Skill-Library.md MOC."""
    by_category = {}
    for s in skills:
        by_category.setdefault(s["category"], []).append(s)

    lines = [
        "---",
        "title: Skill Library — 7Ei",
        "created: 2026-06-22",
        "tags: [org/7ei, skills, library]",
        "status: active",
        "---",
        "",
        "# Skill Library",
        "",
        "> Canonical registry. Generated from `7Ei_OS/skills/catalog.md`.",
        "> **Do not edit manually — edit catalog.md and re-run `sync_vault.py`.**",
        "",
        "---",
        "",
    ]

    for category in CATEGORY_EMOJI:
        if category not in by_category:
            continue
        emoji = CATEGORY_EMOJI.get(category, "📁")
        lines.append(f"## {emoji} {category}")
        lines.append("")
        for s in sorted(by_category[category], key=lambda x: x["name"]):
            try:
                rel = s["skill_file"].relative_to(REPO_ROOT) if s["skill_file"].exists() else None
            except ValueError:
                rel = s["skill_file"] if s["skill_file"].exists() else None
            path_bit = f"`{rel}`" if rel else s["description"]
            lines.append(f"- [[{category}/{s['name']}]] — {path_bit}")
        lines.append("")

    from datetime import date
    lines.extend([
        "---",
        "",
        "## 🔄 Sync Protocol",
        "",
        "**catalog.md is the single source of truth.**",
        "",
        "When adding/editing a skill:",
        "1. Edit `7Ei_OS/skills/<name>/SKILL.md`",
        "2. Update `7Ei_OS/skills/catalog.md`",
        "3. Run `python3 skills/sync_vault.py --vault /Users/artutito/7Ei-MC_TARCO/vault`",
        "4. Commit + PR to 7Ei_OS **and** commit regenerated vault notes in 7Ei-MC_TARCO",
        "",
        "## 📁 Skill Sources",
        "",
        "| Source | Path |",
        "|---|---|",
        "| 7Ei_OS skills | `7Ei_OS/skills/` (git `Arturito7ei/7Ei_OS`) |",
        "| Obsidian vault | `7Ei-MC_TARCO/vault/Skill-Library/` (generated) |",
        "| Workspace skills | `~/.openclaw/workspace/skills/` (symlinks) |",
        "| Cursor skills | `~/.cursor/skills/<name>/SKILL.md` → symlink to 7Ei_OS when vendored |",
        "",
        f"*Generated: {date.today().isoformat()} by sync_vault.py*",
    ])
    return "\n".join(lines)


# ── Symlink setup ─────────────────────────────────────────────────────────────

def setup_workspace_symlinks(skills: list[dict]):
    """Create symlinks for workspace/7Ei-specific skills only.
    Bundled and plugin skills are NOT symlinked — they live in the OpenClaw install."""
    import shutil
    workspace = WORKSPACE_SKILLS
    workspace.mkdir(parents=True, exist_ok=True)

    # Only symlink skills whose source starts with "workspace" (7Ei-owned)
    workspace_skills = [s for s in skills if s["source"].startswith("workspace")]

    print(f"  [Only {len(workspace_skills)} workspace skills get symlinked]")
    for skill in workspace_skills:
        src = skill["skill_file"].parent.resolve()
        dst = workspace / skill["slug"]
        dst_parent = dst.parent
        dst_parent.mkdir(parents=True, exist_ok=True)

        if dst.is_symlink():
            existing = dst.readlink()
            if existing.resolve() == src:
                print(f"  ✅ {dst.name} (already linked correctly)")
                continue
            dst.unlink()
        elif dst.exists() and dst.is_dir():
            backup = workspace / f"{skill['slug']}_dir_backup"
            if backup.exists():
                shutil.rmtree(backup)
            shutil.move(str(dst), str(backup))
            print(f"  📦 {dst.name}/ backed up → {backup.name}/")
        elif dst.exists():
            dst.unlink()

        dst.symlink_to(src)
        print(f"  🔗 {dst.name} → {src.relative_to(REPO_ROOT)}/")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sync Obsidian vault from catalog.md")
    parser.add_argument("--dry-run", action="store_true", help="Print without writing files")
    parser.add_argument("--vault", type=Path, help="Override Obsidian vault path")
    parser.add_argument("--workspace", type=Path, help="Override workspace skills path")
    args = parser.parse_args()

    global OBSIDIAN_VAULT, WORKSPACE_SKILLS, SKILL_LIBRARY_DIR
    if args.vault:
        OBSIDIAN_VAULT = args.vault.resolve()
        SKILL_LIBRARY_DIR = OBSIDIAN_VAULT / "Skill-Library"
    if args.workspace:
        WORKSPACE_SKILLS = args.workspace.resolve()

    vault_dir = SKILL_LIBRARY_DIR if not args.dry_run else None

    print(f"📖 Reading catalog: {CATALOG_PATH}")
    skills = parse_catalog(CATALOG_PATH)
    print(f"✅ Found {len(skills)} skills")

    # Group by category
    by_cat = {}
    for s in skills:
        by_cat.setdefault(s["category"], []).append(s)

    if not args.dry_run:
        # ── Generate category notes ─────────────────────────────────────────
        for category, cat_skills in by_cat.items():
            cat_dir = vault_dir / category.replace(" ", "-")
            cat_dir.mkdir(parents=True, exist_ok=True)

            for skill in sorted(cat_skills, key=lambda x: x["name"]):
                note_path = cat_dir / f"{skill['name']}.md"
                content = generate_obsidian_note(skill)
                note_path.write_text(content)
                print(f"  📄 {category}/{skill['name']}")

        # ── Generate MOC ───────────────────────────────────────────────────
        moc_path = vault_dir / "Skill-Library.md"
        moc_path.write_text(generate_moc(skills))
        print(f"  📋 MOC written: Skill-Library.md")

        # ── Setup symlinks ─────────────────────────────────────────────────
        print(f"\n🔗 Setting up workspace symlinks → {WORKSPACE_SKILLS}")
        setup_workspace_symlinks(skills)
    else:
        print("\n[DRY RUN — no files written]")
        print(f"\nWould generate {len(skills)} skill notes across {len(by_cat)} categories:")
        for cat, cat_skills in sorted(by_cat.items()):
            print(f"\n  {CATEGORY_EMOJI.get(cat, '📁')} {cat}")
            for s in sorted(cat_skills, key=lambda x: x["name"]):
                print(f"    • {s['name']}")

    print(f"\n✅ Sync complete")


if __name__ == "__main__":
    main()
