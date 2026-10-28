# Quadratische Gleichung mit Claude Code: Spezifikation, Tests, Quality Gate

Dieses Repo ist ein Demo-Baukasten. Er zeigt, wie KI-gestützte Code-Entwicklung mit **Claude Code** funktioniert, wenn man sie gegen eine **Spezifikation** und **automatische Tests** prüft. Das Beispiel ist klein absichtlich: eine quadratische Gleichung, deren Lösung man in wenigen Zeilen Python berechnen kann.

Die Kernbotschaft: Man muss den Code nicht selbst lesen können. Man muss aber sagen können, **was richtig ist**. Die Spezifikation und die Tests sind genau dieses „Richtig“, und ein Quality Gate prüft es automatisch.

## Die Aufgabe

Gelöst wird die Gleichung

    y = x² + p·x + q,   y = 0

mit den Lösungen

    x₁,₂ = −p/2 ± √((p/2)² − q)

Die Diskriminante D = (p/2)² − q entscheidet:

- D > 0: zwei reelle Lösungen
- D = 0: eine Lösung
- D < 0: keine reelle Lösung

## Was im Repo liegt

| Datei / Ordner | Zweck |
|---|---|
| [DEMO_SKRIPT.md](DEMO_SKRIPT.md) | Ablauf einer Live-Demo mit Zeiten, Sprechpunkten und Risiken |
| [PROMPTS.md](PROMPTS.md) | Alle Prompts zum Kopieren, in der richtigen Reihenfolge |
| [neues-demo-projekt.sh](neues-demo-projekt.sh) | Erzeugt aus der Vorlage ein frisches Projekt mit eigenem Git-Repo |
| [vorlage/](vorlage/) | Der Startzustand des Demo-Projekts |

In der Vorlage:

- `CLAUDE.md`: Projektregeln, die Claude Code bei jedem Start liest (Sprache, Test-first, Quality Gate)
- `check.py`: das Quality Gate. Es führt ruff (Stil), mypy (Typen) und pytest (Tests, mindestens 90 % Abdeckung) aus und zeigt pro Schritt ✅ oder ❌
- `pyproject.toml`, `requirements-dev.txt`: Konfiguration und Entwicklungswerkzeuge
- `src/quadratic/`: hier entsteht der Code, zu Beginn nur eine leere `__init__.py`
- `tests/`: hier entstehen die Tests, zu Beginn leer

## Ablauf: der Kreislauf

    Spezifikation  →  Tests (zuerst rot)  →  Code  →  Quality Gate (grün)

1. **Spezifikation:** Claude Code schreibt aus einer groben Beschreibung eine `SPEC.md` mit nummerierten Akzeptanzkriterien (AK-1, AK-2 …).
2. **Tests zuerst:** Die Tests entstehen aus der Spezifikation, bevor es Code gibt. Sie müssen rot sein. Das zeigt, dass sie wirklich etwas prüfen.
3. **Code:** Claude Code implementiert, bis alle Tests grün sind.
4. **Quality Gate:** `python check.py` prüft Stil, Typen, Tests und Abdeckung. Nur wenn alles grün ist, gilt ein Schritt als fertig.
5. **Mutationstest:** Ein absichtlicher Fehler im Code (z. B. ein Vorzeichen) muss das Gate rot werden lassen. So sieht man, dass die Tests den Fehler tatsächlich finden.

## Schnellstart

Voraussetzungen: Python 3.11 oder neuer, Git, Bash und ein Zugang zu Claude Code.

```bash
git clone https://github.com/<benutzer>/quadratic-equation.git
cd quadratic-equation
./neues-demo-projekt.sh          # legt ../quadratic-demo an
cd ../quadratic-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
claude                           # Claude Code im Demo-Projekt starten
```

Danach führst du die Prompts aus [PROMPTS.md](PROMPTS.md) der Reihe nach aus. Zum Prüfen jederzeit:

```bash
python check.py
```

Das Demo-Projekt ist bewusst getrennt vom Repo. So bleibt die Vorlage sauber, und du kannst die Demo beliebig oft neu durchspielen.

## Hinweis zur Formel

In einer frühen Fassung stand `y = x*x + p + q`. Gemeint ist `y = x² + p·x + q`, denn ohne `x` bei `p` gäbe es nichts zu lösen. Die Spezifikation legt die Formel vor dem ersten Code eindeutig fest. Das ist auch ein Beispiel dafür, warum Klärung vor Code wichtig ist.

## Lizenz

Noch nicht festgelegt.
