"""Quality Gate: Stil, Typen, Tests und Testabdeckung müssen bestehen."""

import subprocess
import sys

MIN_COVERAGE = 90

STEPS = [
    ("Stil (ruff)", [sys.executable, "-m", "ruff", "check", "src", "tests"]),
    ("Typen (mypy)", [sys.executable, "-m", "mypy", "src"]),
    (
        f"Tests + Abdeckung >= {MIN_COVERAGE} % (pytest)",
        [
            sys.executable, "-m", "pytest", "-q",
            "--cov=quadratic", "--cov-report=term-missing",
            f"--cov-fail-under={MIN_COVERAGE}",
        ],
    ),
]


def main() -> int:
    failed = []
    for name, cmd in STEPS:
        print(f"\n=== {name} ===", flush=True)
        if subprocess.run(cmd).returncode != 0:
            failed.append(name)

    print("\n" + "=" * 50)
    if failed:
        print("❌ QUALITY GATE NICHT BESTANDEN")
        for name in failed:
            print(f"   - {name}")
        return 1
    print("✅ QUALITY GATE BESTANDEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
