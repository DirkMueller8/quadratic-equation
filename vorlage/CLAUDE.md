# Projekt: Quadratische Gleichung x² + p·x + q = 0

## Regeln
- Sprache der Doku und Kommentare: Deutsch; Code-Bezeichner: Englisch
- Die Spezifikation steht in SPEC.md. Sie ist die einzige Wahrheit.
- Immer zuerst Tests schreiben, dann Code (Test-first). Testnamen verweisen auf die AK-Nummer (z. B. `test_ak1_...`).
- Kein Sprint gilt als fertig, bevor `python check.py` grün ist (Quality Gate).
- Keine neuen Abhängigkeiten ohne Rückfrage. Nur Python-Standardbibliothek für den Produktivcode.
- Änderungen an Verhalten: erst SPEC.md, dann Tests, dann Code.

## Quality Gate sichtbar machen (wichtig für Live-Demos)
Die Tool-Ausgabe ist im Terminal eingeklappt. Deshalb gilt:
- Führe `python check.py` nach **jeder** Änderung an Tests oder Code selbst aus, auch ohne Aufforderung. Nie nur `pytest` allein.
- Gib das Ergebnis **immer wörtlich in deiner Antwort** wieder, als Codeblock mit den Zeilen ✅/❌ und der Schlusszeile (QUALITY GATE BESTANDEN / NICHT BESTANDEN).
- Wenn das Gate rot ist, nenne in einem Satz den Grund (z. B. „Tests schlagen fehl, weil solve() noch nicht existiert“).
- In der Test-first-Phase ist ein rotes Gate das **erwartete** Ergebnis: Sag das ausdrücklich, und implementiere dann noch nichts.
- Keine Tests schreiben, die bereits grün sind, wenn der Code fehlt. Prüfe vor dem Schreiben von Tests, ob `src/quadratic/` nur `__init__.py` enthält.

## Struktur
- `src/quadratic/` Produktivcode
- `tests/` pytest-Tests
- `check.py` Quality Gate (ruff, mypy, pytest + Abdeckung ≥ 90 %)
- `SPEC.md` Spezifikation (wird sprintweise erweitert)

## Befehle
- Quality Gate: `python check.py`
- Nur Tests: `python -m pytest`
