#!/usr/bin/env python3
"""Dependency-free structural validation for the skills in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML delimiter")
    try:
        raw, _body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("missing closing YAML delimiter") from exc

    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]

    try:
        values = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [str(exc)]

    if set(values) != {"name", "description"}:
        errors.append("frontmatter must contain exactly name and description")
    if values.get("name") != skill_dir.name:
        errors.append("frontmatter name must match directory name")
    if not NAME_RE.fullmatch(values.get("name", "")):
        errors.append("name must be lowercase hyphen-case")
    description = values.get("description", "")
    if not 20 <= len(description) <= 1024:
        errors.append("description must be 20-1024 characters")
    if "TODO" in skill_file.read_text(encoding="utf-8"):
        errors.append("SKILL.md contains TODO")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.is_file():
        errors.append("missing agents/openai.yaml")
    elif f"${skill_dir.name}" not in openai_yaml.read_text(encoding="utf-8"):
        errors.append("default prompt does not mention the skill explicitly")
    return errors


def main() -> int:
    if not SKILLS.is_dir():
        print("ERROR: skills directory not found", file=sys.stderr)
        return 1
    failures = 0
    for skill_dir in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        errors = validate(skill_dir)
        if errors:
            failures += 1
            for error in errors:
                print(f"FAIL {skill_dir.name}: {error}")
        else:
            print(f"OK   {skill_dir.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
