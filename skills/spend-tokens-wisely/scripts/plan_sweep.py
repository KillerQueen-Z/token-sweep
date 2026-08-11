#!/usr/bin/env python3
"""Recommend a useful, non-overlapping token-sweep portfolio."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Lane:
    skill: str
    minutes: int
    focuses: tuple[str, ...]
    value: int
    scope: str


LANES = (
    Lane("review-repository-deeply", 7, ("correctness",), 92, "recent diff or one risky path"),
    Lane("audit-docs-drift", 18, ("docs", "correctness"), 66, "public docs and examples"),
    Lane("audit-dependency-health", 25, ("dependencies",), 76, "one package ecosystem"),
    Lane("find-test-gaps", 30, ("testing", "correctness"), 88, "one critical user journey"),
    Lane("profile-performance-risks", 40, ("performance",), 75, "one request, job, or data path"),
    Lane("map-architecture-debt", 45, ("architecture",), 72, "one subsystem"),
    Lane("review-repository-deeply", 55, ("correctness", "security"), 96, "whole small repo or critical subsystem"),
)

VALID_FOCUSES = {
    "balanced",
    "correctness",
    "testing",
    "docs",
    "architecture",
    "dependencies",
    "performance",
    "security",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minutes", type=int, required=True, help="available wall-clock minutes")
    parser.add_argument(
        "--focus",
        default="balanced",
        help="comma-separated: correctness,testing,docs,architecture,dependencies,performance; security routes to a specialist",
    )
    parser.add_argument("--repo-size", choices=("small", "medium", "large"), default="medium")
    parser.add_argument("--risk", choices=("report-only", "safe-fixes"), default="report-only")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args()


def choose(minutes: int, focuses: set[str], repo_size: str) -> list[Lane]:
    if minutes < 5:
        return []
    reserve = min(minutes, max(3, round(minutes * 0.15)))
    budget = max(1, minutes - reserve)

    def score(lane: Lane) -> float:
        focus_bonus = 100 if "balanced" in focuses or focuses.intersection(lane.focuses) else 0
        size_penalty = 18 if repo_size == "large" and "whole" in lane.scope else 0
        return lane.value + focus_bonus - size_penalty - lane.minutes / 10

    candidates = [lane for lane in LANES if lane.minutes <= budget]
    variants: dict[str, list[Lane]] = {}
    for lane in candidates:
        variants.setdefault(lane.skill, []).append(lane)
    candidates = []
    for skill_lanes in variants.values():
        if repo_size == "large" and minutes < 90:
            candidates.append(max(skill_lanes, key=score))
        else:
            candidates.append(max(skill_lanes, key=lambda lane: lane.minutes))
    candidates.sort(key=score, reverse=True)
    selected: list[Lane] = []
    used_skills: set[str] = set()
    for lane in candidates:
        if lane.skill in used_skills or lane.minutes > budget:
            continue
        selected.append(lane)
        used_skills.add(lane.skill)
        budget -= lane.minutes
        if len(selected) == 3:
            break
    return selected


def main() -> int:
    args = parse_args()
    if args.minutes <= 0:
        raise SystemExit("--minutes must be positive")
    focuses = {item.strip().lower() for item in args.focus.split(",") if item.strip()}
    focuses = focuses or {"balanced"}
    unknown = focuses - VALID_FOCUSES
    if unknown:
        raise SystemExit(f"unknown focus: {', '.join(sorted(unknown))}")
    reserve = min(args.minutes, max(3, round(args.minutes * 0.15)))
    if "security" in focuses:
        result = {
            "timebox_minutes": args.minutes,
            "synthesis_reserve_minutes": reserve,
            "risk": args.risk,
            "lanes": [],
            "specialist_required": "security-audit",
        }
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(f"Token Sweep: {args.minutes} minutes, {args.risk}")
            print("Security focus requires an installed dedicated security-audit workflow; no generic lane was substituted.")
        return 0
    selected = choose(args.minutes, focuses, args.repo_size)
    result = {
        "timebox_minutes": args.minutes,
        "synthesis_reserve_minutes": reserve,
        "risk": args.risk,
        "lanes": [asdict(lane) for lane in selected],
    }
    if args.format == "json":
        print(json.dumps(result, indent=2))
        return 0

    print(f"Token Sweep: {args.minutes} minutes, {args.risk}")
    if not selected:
        print("No credible sweep fits. Pick one changed file and request a focused review.")
        return 0
    for index, lane in enumerate(selected, 1):
        print(f"{index}. ${lane.skill} ({lane.minutes} min) — {lane.scope}")
    print(f"Reserve ~{result['synthesis_reserve_minutes']} min to deduplicate and rank findings.")
    names = ", ".join(f"${lane.skill}" for lane in selected)
    print(f"Prompt: Use {names} in {args.risk} mode. Keep scopes independent and return one ranked report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
