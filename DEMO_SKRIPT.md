# Demo-Skript: Claude Code – Spezifikation → Tests → Quality Gates

Dauer: ca. 30 min. Publikum: keine Claude-Code-, kaum Programmiererfahrung, M365-Copilot-Chat bekannt.
Alle Prompts zum Kopieren: [PROMPTS.md](PROMPTS.md)

**Dieses Repo ist das Regiebuch.** Die Demo selbst läuft in einem separaten Projekt (`quadratic-demo`), das aus [vorlage/](vorlage/) erzeugt wird. Das Publikum sieht nur das Demo-Projekt, nie dieses Skript.

## Wichtig vorab: die Formel
Problemstellung: **y = x² + p·x + q**, gelöst wird y = 0.

x₁,₂ = −p/2 ± √((p/2)² − q), Diskriminante D = (p/2)² − q
D > 0: zwei Lösungen · D = 0: eine Lösung · D < 0: keine reelle Lösung

## Scope
- Sprint 1: Backend (Lösung berechnen), inkl. Mutationstest
- Sprint 2: Datei `ergebnis.csv` mit Kopfzeile. Testfälle und manuelle Eingaben werden Zeile für Zeile angehängt.

## Vorbereitung (vorab)
1. **Zurücksetzen für die echte Demo:** Probe-Ordner löschen und umbenennen von hier aus im Terminal (`rm -rf ./quadratic-demo-probe && mv ./quadratic-demo ./quadratic-demo-probe`) und `./neues-demo-projekt.sh`, venv neu einrichten.

2. Demo-Projekt von hier aus im Terminal erzeugen: `./neues-demo-projekt.sh` (legt `../quadratic-demo` mit eigenem Git-Repo an).

3. Neues VS Code `quadratic-demo` öffnen, NICHT in diesem Repo. Terminal öffnen und `Claude` im Prompt eingeben. Danach: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.txt` (falls venv fehlschlägt: `sudo apt install python3.14-venv`).

4. Prüfen: `python -m ruff --version && python -m mypy --version && python -m pytest --version`

5. Terminal-Schrift ≥ 18 pt (Ctrl +), Benachrichtigungen aus, Prompts aus PROMPTS.md bereit.

6. **Gate-Ergebnis sichtbar:** Claude Code klappt Tool-Ausgaben ein („Ran 1 shell command“). Deshalb steht in `CLAUDE.md`, dass Claude `python check.py` selbst ausführt und das Ergebnis (✅/❌) wörtlich wiedergibt. 
Sonst `python check.py` selbst im Terminal ausführen.

7. Vor Prompt 1.2 und 2.2: `ls src/quadratic` prüfen. Vor 1.2 darf dort nur `__init__.py` stehen, sonst sind die Tests sofort grün.

8. `check.py` ist bewusst schon vorhanden und ist rot, solange es keine Tests gibt („Keine Tests gefunden“).

## Demo
- Copilot-Chat: antwortet mit Text, du kopierst. Claude Code: arbeitet im Projektordner, liest, schreibt Dateien, startet Programme, korrigiert sich selbst.
- Kreislauf als Bild: **Spezifikation → Tests → Code → Quality Gate** (rot: zurück zum Code, grün: fertig).
- Kernbotschaft: **Wir müssen den Code nicht lesen können, wir müssen sagen können, was richtig ist.**
- Analogie: Bauauftrag (Spezifikation), Abnahmeprotokoll (Tests), Bauabnahme (Quality Gate).
- Kurz `CLAUDE.md` zeigen (Regeln einmal festlegen) und `check.py` (das Quality Gate).

### Sprint 1: Backend (15 Min.)
1. **Spezifikation (3 Min.)** Prompt 1.1. Claude stellt Rückfragen: laut beantworten. Botschaft: Klärung vor Code ist billiger als Fehler danach. `SPEC.md` kurz in der IDE zeigen.
   Erwartete Akzeptanzkriterien (Beispiele):
   - AK-1: p=−3, q=2 → (1, 2)
   - AK-2: p=2, q=1 → eine Lösung (−1)
   - AK-3: p=0, q=1 → keine reelle Lösung
   - AK-4: Jede Lösung erfüllt die Gleichung (Probe, Toleranz 1e-9)

2. **Tests zuerst (3 Min.)** Prompt 1.2. **Wow-Moment 1:** Rot ist gewollt: „So wissen wir, dass die Tests wirklich etwas prüfen.“

3. **Implementieren (3 Min.)** Prompt 1.3. Claude liest Fehlermeldungen und korrigiert selbst. Gate ✅.

4. Still sichern (Prompt 1.4), `git status --short` leer.

5. **Mutationstest (5 Min.) – stärkster Moment.** In der IDE ein Vorzeichen kippen, speichern, selbst `python check.py` → ❌. „Ich habe Code manipuliert, ohne ihn lesen zu müssen, das Gate merkt es sofort.“ Zurück: `git checkout src/`, Gate wieder ✅. Tag nur in der Generalprobe.

### Sprint 2: Ergebnis als CSV (10 Min.)
1. `/clear`. **Spezifikation (3 Min.)** Prompt 2.1. Claude muss entscheiden: Semikolon + Dezimalkomma oder Komma + Dezimalpunkt. Frage ans Publikum: „Wer hat eine CSV schon mal in Excel geöffnet, und alles stand in einer Spalte?“ Spezifikationen beseitigen solche Überraschungen.

2. **Tests (rot) und Implementierung (5 Min.)** Prompt 2.2, dann 2.3.

3. **Vorführen (2 Min.)** Prompt 2.4. Startskript zweimal manuell laufen lassen, danach `ergebnis.csv` in Excel öffnen: Zeile für Zeile kommt dazu.

### Fazit (5 Min.)
1. **Spezifikation** = „Was soll richtig sein?“ (menschliche Aufgabe)
2. **Tests** = „Ist es richtig?“ (maschinell, wiederholbar)
3. **Quality Gate** = „Darf es weiter?“ (automatisch, unbestechlich)

Brücke in den Alltag: Spezifikation, Prüfkriterien und Abnahme funktionieren auch für Excel-Auswertungen, Berichte und Prozesse.
Ehrlich bleiben: KI-Code ist nicht automatisch richtig. **Die Qualität kommt aus den Tests, nicht aus dem Modell.**

## Notausgang bei Zeitnot
Nach Sprint 1 abbrechen und zum Fazit springen: Der Kern (Spezifikation, rote Tests, Code, grünes Gate, Mutationstest) ist gezeigt. Optional im Probe-Ordner `git checkout sprint2-fertig` und das fertige CSV zeigen (offen sagen: „vorher vorbereitet“).

## Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| Claude braucht zu lange | Generalprobe mit Stoppuhr. Fallback: Git-Tag im Probe-Ordner. |
| Ergebnis weicht vom Probelauf ab | Das ist ein Feature: Das Gate fängt Abweichungen ab. Offen sagen. |
| Berechtigungsdialoge | Vorab typische Freigaben erlauben (`/fewer-permission-prompts`). Sonst kurz erklären: „Claude fragt, bevor es etwas ausführt.“ |
| Netzwerk fällt aus | Hotspot, Screenshots/Video des Probelaufs als Plan C |
| Beamer-Lesbarkeit | Schrift groß, jeweils nur das Wichtige zeigen |

## Checkliste Generalprobe
- [ ] Gesamtdurchlauf mit Stoppuhr
- [ ] Beide Tags gesetzt, Wiederherstellung getestet
- [ ] Mutationszeile notiert
- [ ] Gate-Ergebnis erscheint in Claudes Antwort
- [ ] Anmeldung bei Claude Code und Netzwerk vorher getestet
