from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "spend-tokens-wisely"
    / "scripts"
    / "plan_sweep.py"
)
SPEC = importlib.util.spec_from_file_location("plan_sweep", SCRIPT)
assert SPEC and SPEC.loader
PLAN_SWEEP = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = PLAN_SWEEP
SPEC.loader.exec_module(PLAN_SWEEP)


class ChoosePortfolioTests(unittest.TestCase):
    def test_focus_prefers_matching_lanes(self) -> None:
        lanes = PLAN_SWEEP.choose(60, {"correctness", "testing"}, "medium")
        self.assertEqual(
            [lane.skill for lane in lanes],
            ["review-repository-deeply", "find-test-gaps"],
        )

    def test_long_timebox_upgrades_to_deep_review(self) -> None:
        lanes = PLAN_SWEEP.choose(90, {"correctness"}, "medium")
        review = next(lane for lane in lanes if lane.skill == "review-repository-deeply")
        self.assertEqual(review.minutes, 55)

    def test_large_repo_narrows_before_ninety_minutes(self) -> None:
        lanes = PLAN_SWEEP.choose(80, {"correctness"}, "large")
        review = next(lane for lane in lanes if lane.skill == "review-repository-deeply")
        self.assertEqual(review.minutes, 7)

    def test_individual_focus_routes_to_matching_lane(self) -> None:
        cases = {
            "docs": (25, "audit-docs-drift"),
            "architecture": (60, "map-architecture-debt"),
            "dependencies": (35, "audit-dependency-health"),
            "performance": (55, "profile-performance-risks"),
            "testing": (40, "find-test-gaps"),
        }
        for focus, (minutes, expected) in cases.items():
            with self.subTest(focus=focus):
                lanes = PLAN_SWEEP.choose(minutes, {focus}, "medium")
                self.assertEqual(lanes[0].skill, expected)

    def test_portfolio_is_bounded_and_unique(self) -> None:
        for minutes in (10, 30, 60, 120):
            lanes = PLAN_SWEEP.choose(minutes, {"balanced"}, "medium")
            reserve = min(minutes, max(3, round(minutes * 0.15)))
            self.assertLessEqual(sum(lane.minutes for lane in lanes), minutes - reserve)
            names = [lane.skill for lane in lanes]
            self.assertEqual(len(names), len(set(names)))
            self.assertLessEqual(len(names), 3)

    def test_useful_boundary_starts_at_ten_minutes(self) -> None:
        self.assertEqual(PLAN_SWEEP.choose(9, {"balanced"}, "small"), [])
        self.assertEqual(len(PLAN_SWEEP.choose(10, {"balanced"}, "small")), 1)

    def test_tiny_timebox_returns_no_lane(self) -> None:
        self.assertEqual(PLAN_SWEEP.choose(4, {"balanced"}, "small"), [])


class CliContractTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_json_contract_and_risk(self) -> None:
        result = self.run_cli(
            "--minutes", "60", "--focus", " Testing , CORRECTNESS ",
            "--repo-size", "medium", "--risk", "safe-fixes", "--format", "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["risk"], "safe-fixes")
        self.assertEqual(payload["timebox_minutes"], 60)
        self.assertTrue(payload["lanes"])

    def test_security_requires_specialist(self) -> None:
        result = self.run_cli("--minutes", "30", "--focus", "security", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["lanes"], [])
        self.assertEqual(payload["specialist_required"], "security-audit")

    def test_unknown_focus_fails(self) -> None:
        result = self.run_cli("--minutes", "30", "--focus", "correctnes")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown focus", result.stderr)

    def test_non_positive_minutes_fail(self) -> None:
        result = self.run_cli("--minutes", "0")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be positive", result.stderr)

    def test_tiny_json_reserve_is_capped(self) -> None:
        result = self.run_cli("--minutes", "1", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["synthesis_reserve_minutes"], 1)


if __name__ == "__main__":
    unittest.main()
