#!/usr/bin/env python3
"""
Run all seed scripts in the correct order.

Usage (from project root):
    cd ~/Desktop/comptia_quiz
    python3 seeds/run_all.py
"""

import subprocess
import sys
import os

# Run from project root regardless of where script is called from
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(project_root)
sys.path.insert(0, project_root)

seeds = [
    # ── IT Fundamentals ───────────────────────────────────────────
    "seeds/seed_it_fundamentals.py",

    # ── Core 1 — General ──────────────────────────────────────────
    "seeds/seed_complete.py",
    "seeds/seed_new_questions.py",
    "seeds/seed_top50.py",
    "seeds/seed_troubleshooting_core1.py",
    "seeds/seed_multi_select.py",

    # ── Core 1 — Mobile Devices ───────────────────────────────────
    "seeds/seed_laptop_hardware.py",
    "seeds/seed_study_guide_q16_37.py",
    "seeds/seed_mobile_connectivity.py",
    "seeds/seed_mobile_optimization.py",
    "seeds/seed_mobile_extra.py",
    "seeds/seed_mobile_advanced.py",
    "seeds/seed_missing_objectives.py",

    # ── Core 1 — Networking ───────────────────────────────────────
    "seeds/seed_networking_and_scenarios.py",
    "seeds/seed_networking_objectives.py",

    # ── Core 1 — Ports & Protocols ────────────────────────────────
    "seeds/seed_ports_protocols.py",
    "seeds/seed_ports_extended.py",

    # ── Core 1 — Exam Practice ────────────────────────────────────
    "seeds/seed_exam_practice.py",
    "seeds/seed_exam_practice2.py",

    # ── Core 2 ────────────────────────────────────────────────────
    "seeds/seed_core2_batch1.py",
    "seeds/seed_core2_batch2.py",
    "seeds/seed_core2_batch3.py",
    "seeds/seed_core2_batch4.py",
    "seeds/seed_core2_batch5.py",
    "seeds/seed_core2_batch6.py",
    "seeds/seed_core2_batch7.py",
    "seeds/seed_core2_batch8.py",
    "seeds/seed_core2_final.py",
]

print("=" * 60)
print("  CompTIA A+ Prep — Database Seeder")
print("=" * 60)
print()

total_added = 0
total_skipped = 0
errors = []

for seed in seeds:
    if not os.path.exists(seed):
        print(f"⚠️  SKIP (not found): {seed}")
        continue

    name = os.path.basename(seed)
    print(f"▶  {name}...", end=" ", flush=True)

    result = subprocess.run(
        [sys.executable, seed],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        for line in result.stdout.strip().split('\n'):
            if 'Added' in line:
                print(f"✅  {line}")
                try:
                    parts = line.split()
                    total_added += int(parts[parts.index('Added') + 1])
                    total_skipped += int(parts[parts.index('Skipped') + 1])
                except:
                    pass
    else:
        print(f"❌  ERROR")
        errors.append((name, result.stderr[-300:]))

print()
print("=" * 60)
print(f"  Done!  Added: {total_added}  |  Skipped: {total_skipped}")
if errors:
    print(f"\n  ⚠️  {len(errors)} error(s):")
    for name, err in errors:
        print(f"     {name}: {err}")
print("=" * 60)