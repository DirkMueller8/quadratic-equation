# Projekt: Quadratische Gleichung x² + p·x + q = 0

## Regeln
- Sprache der Doku und Kommentare: Deutsch; Code-Bezeichner: Englisch
- Die Spezifikation steht in SPEC.md. Sie ist die einzige Wahrheit.
- Immer zuerst Tests schreiben, dann Code (Test-first). Testnamen verweisen auf die AK-Nummer (z. B. `test_ak1_...`).
- Kein Sprint gilt als fertig, bevor `python check.py` grün ist (Quality Gate).
- Keine neuen Abhängigkeiten ohne Rückfrage. Nur Python-Standardbibliothek für den Produktivcode.
- Änderungen an Verhalten: erst SPEC.md, dann Tests, dann Code.

## Struktur
- `src/quadratic/` Produktivcode
- `tests/` pytest-Tests
- `check.py` Quality Gate (ruff, mypy, pytest + Abdeckung ≥ 90 %)
- `SPEC.md` Spezifikation (wird sprintweise erweitert)

## Befehle
- Quality Gate: `python check.py`
- Nur Tests: `python -m pytest`
