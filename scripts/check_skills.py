#!/usr/bin/env python3
"""Check the IntentFlow skills and README before they are merged or released.

Run from anywhere:  python scripts/check_skills.py
Exits with status 1 and lists every problem if a check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX = 64
DESCRIPTION_MAX = 1024
RESERVED_WORDS = ("claude", "anthropic")
LONG_SKILL_LINES = 500

errors: list[str] = []
warnings: list[str] = []


def check_skill(folder: Path) -> None:
    skill_file = folder / "SKILL.md"
    label = f"skills/{folder.name}"
    if not skill_file.is_file():
        errors.append(f"{label}: missing SKILL.md")
        return

    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        errors.append(f"{label}: SKILL.md must start with YAML frontmatter between '---' lines")
        return

    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{label}: frontmatter is not valid YAML ({exc})")
        return
    body = match.group(2)

    name = meta.get("name")
    if not isinstance(name, str) or not name:
        errors.append(f"{label}: frontmatter needs a 'name'")
    else:
        if name != folder.name:
            errors.append(f"{label}: name '{name}' must match the folder name")
        if not NAME_PATTERN.match(name):
            errors.append(f"{label}: name '{name}' must use lowercase letters, numbers and hyphens")
        if len(name) > NAME_MAX:
            errors.append(f"{label}: name is {len(name)} characters (max {NAME_MAX})")
        for word in RESERVED_WORDS:
            if word in name:
                errors.append(f"{label}: name must not contain '{word}'")

    description = meta.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{label}: frontmatter needs a 'description'")
    else:
        if len(description) > DESCRIPTION_MAX:
            errors.append(f"{label}: description is {len(description)} characters (max {DESCRIPTION_MAX})")
        if "<" in description or ">" in description:
            errors.append(f"{label}: description must not contain angle brackets")

    if not body.strip():
        errors.append(f"{label}: SKILL.md has no instructions after the frontmatter")
    elif len(body.splitlines()) > LONG_SKILL_LINES:
        warnings.append(f"{label}: {len(body.splitlines())} lines; consider keeping skills under {LONG_SKILL_LINES}")


def check_readme(skill_names: list[str]) -> None:
    if not README.is_file():
        errors.append("README.md is missing")
        return
    text = README.read_text(encoding="utf-8")

    layout = re.search(r"```text\nintentflow-skills/\n(.*?)```", text, re.S)
    if not layout:
        errors.append("README.md: 'Repository layout' block starting with intentflow-skills/ not found")
    else:
        listed = sorted(set(re.findall(r"(intentflow-[a-z0-9-]+)/SKILL\.md", layout.group(1))))
        for name in sorted(set(skill_names) - set(listed)):
            errors.append(f"README.md: repository layout is missing skills/{name}")
        for name in sorted(set(listed) - set(skill_names)):
            errors.append(f"README.md: repository layout lists skills/{name}, which doesn't exist")

    for name in skill_names:
        if f"`{name}`" not in text:
            errors.append(f"README.md: the team table doesn't mention `{name}`")

    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        path = (ROOT / target.split("#")[0]).resolve()
        if not path.exists():
            errors.append(f"README.md: link to '{target}' points to a file that doesn't exist")


def main() -> int:
    folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.is_dir() else []
    if not folders:
        errors.append("skills/: no skill folders found")
    for folder in folders:
        check_skill(folder)
    check_readme([f.name for f in folders])

    for message in warnings:
        print(f"warning: {message}")
    if errors:
        for message in errors:
            print(f"error: {message}")
        print(f"\n{len(errors)} problem(s) found in {len(folders)} skills.")
        return 1
    print(f"All checks passed for {len(folders)} skills and the README.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
