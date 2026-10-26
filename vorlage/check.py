"""Quality Gate: Stil, Typen, Tests und Testabdeckung müssen bestehen.

Ausgabe: eine Zeile pro Schritt (✅/❌). Details nur bei Fehlern.
"""

import os
import subprocess
import sys

MIN_COVERAGE = 90
NO_TESTS_EXIT_CODE = 5  # pytest: es wurden keine Tests gefunden

STEPS = [
    ("Stil (ruff)", [sys.executable, "-m", "ruff", "check", "src", "tests"]),
    ("Typen (mypy)", [sys.executable, "-m", "mypy", "src"]),
    (
        f"Tests + Abdeckung >= {MIN_COVERAGE} % (pytest)",
        [
            sys.executable, "-m", "pytest", "-q",
            "-W", "ignore::coverage.exceptions.CoverageWarning",
            "-W", "ignore::pytest_cov.plugin.CovReportWarning",
            "--cov=quadratic", "--cov-report=term-missing:skip-covered",
            f"--cov-fail-under={MIN_COVERAGE}",
        ],
    ),
]


def run_step(name: str, cmd: list[str]) -> bool:
    # Kein Bytecode-Cache: Eine Code-Änderung wird immer sofort wirksam
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    output = (result.stdout + result.stderr).strip()
    ok = result.returncode == 0
    print(f"{'✅' if ok else '❌'} {name}")
    if ok:
        return True
    if result.returncode == NO_TESTS_EXIT_CODE or "no tests ran" in output:
        print("     Keine Tests gefunden: Es gibt nichts, was den Code prüft.")
    else:
        for line in output.splitlines()[-25:]:
            print(f"     {line}")
    return False


def main() -> int:
    failed = [name for name, cmd in STEPS if not run_step(name, cmd)]

    print("=" * 50)
    if failed:
        print("❌ QUALITY GATE NICHT BESTANDEN")
        return 1
    print("✅ QUALITY GATE BESTANDEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
