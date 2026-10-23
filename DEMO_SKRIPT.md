# Demo-Skript: Claude Code – Spezifikation → Tests → Quality Gates

Dauer: ca. 50 Min. plus 10 Min. Puffer. Publikum: keine Claude-Code-, kaum Programmiererfahrung, M365-Copilot-Chat bekannt.
Alle Prompts zum Kopieren: [PROMPTS.md](PROMPTS.md)

## Wichtig vorab: die Formel
`y = x*x + p + q` ist vermutlich ein Tippfehler. Gemeint: **y = x² + p·x + q**, gelöst wird y = 0.

x₁,₂ = −p/2 ± √((p/2)² − q), Diskriminante D = (p/2)² − q
D > 0: zwei Lösungen · D = 0: eine Lösung · D < 0: keine reelle Lösung

Dramaturgisch nutzbar: Die Spezifikation legt die Formel vor dem ersten Code eindeutig fest.

## Scope (bewusst reduziert)
- Sprint 1: Backend (Lösung berechnen)
- Sprint 2: Historie (wiederholbar, Liste) plus CSV-Export als reine Textfunktion
- Sprint 3: Tabellarische Ausgabe im Terminal (CLI)
- Bonus: Spezifikationsänderung live
- Entfällt: Web-GUI (Risiko: Netzwerk, Ports, Installation, Browser)

## Vorbereitung (vorab)
1. `sudo apt install python3.14-venv` (nur falls `python3 -m venv` fehlschlägt)
2. `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.txt`
3. Prüfen: `python -m ruff --version`, `python -m mypy --version`, `python -m pytest --version`
4. `git init`, erster Commit mit dem Gerüst (CLAUDE.md, check.py, pyproject.toml, …)
5. **Generalprobe komplett durchspielen** und nach jedem Sprint taggen: `sprint1-fertig`, `sprint2-fertig`, `sprint3-fertig`. Danach zurück zum Gerüst-Commit (`git reset --hard <gerüst-commit>`; Tags bleiben erhalten).
6. Terminal-Schrift ≥ 18 pt, Benachrichtigungen aus, Prompts aus PROMPTS.md bereit.
7. Hinweis: `check.py` ist bewusst schon vorhanden und läuft erst grün, wenn Tests und Code existieren. Ohne Tests meldet pytest „no tests ran“ (rot).

## Ablauf

| Zeit | Block |
|---|---|
| 0–8 | Einführung |
| 8–25 | Sprint 1: Backend inkl. Mutationstest |
| 25–37 | Sprint 2: Historie und CSV |
| 37–45 | Sprint 3: CLI-Tabelle |
| 45–52 | Bonus: Spezifikationsänderung |
| 52–60 | Fazit, Fragen (Puffer) |

### Einführung (8 Min.)
- Copilot-Chat: antwortet mit Text, du kopierst. Claude Code: arbeitet im Projektordner, liest, schreibt Dateien, startet Programme, korrigiert sich selbst.
- Kreislauf als Bild: **Spezifikation → Tests → Code → Quality Gate** (rot: zurück zum Code, grün: fertig).
- Kernbotschaft: **Wir müssen den Code nicht lesen können, wir müssen sagen können, was richtig ist.**
- Analogie: Bauauftrag (Spezifikation), Abnahmeprotokoll (Tests), Bauabnahme (Quality Gate).
- Kurz `CLAUDE.md` zeigen: Projektregeln werden einmal festgelegt. Danach `check.py` zeigen: das ist das Quality Gate.

### Sprint 1: Backend (17 Min.)
1. **Spezifikation (3 Min.)** Prompt 1.1. Claude stellt Rückfragen: laut beantworten. Botschaft: Klärung vor Code ist billiger als Fehler danach.
   Erwartete Akzeptanzkriterien (Beispiele):
   - AK-1: p=−3, q=2 → (1, 2)
   - AK-2: p=2, q=1 → eine Lösung (−1)
   - AK-3: p=0, q=1 → keine reelle Lösung
   - AK-4: Jede Lösung erfüllt die Gleichung (Probe, Toleranz 1e-9)
   - AK-5: Nicht-endliche Eingaben (NaN, inf) → ValueError
   - AK-6: Lösungen aufsteigend sortiert
2. **Tests zuerst (4 Min.)** Prompt 1.2. **Wow-Moment 1:** Rot ist gewollt: „So wissen wir, dass die Tests wirklich etwas prüfen.“
3. **Implementieren (3 Min.)** Prompt 1.3. Zuschauen: Claude liest Fehlermeldungen und korrigiert selbst.
4. **Quality Gate (2 Min.)** `python check.py` → ✅ BESTANDEN.
5. **Mutationstest (5 Min.) – stärkster Moment.** Vorzeichen in solver.py kippen, `python check.py` → ❌ AK-1 rot. „Ich habe Code manipuliert, ohne ihn lesen zu müssen, das Gate merkt es sofort.“ Zurück: `git checkout src/`.
6. `git commit`, `git tag sprint1-fertig`.

### Sprint 2: Historie und CSV (12 Min.)
1. **Spezifikation (3 Min.)** Prompt 2.1. Claude muss entscheiden: Semikolon + Dezimalkomma oder Komma + Dezimalpunkt. Frage ans Publikum: „Wer hat eine CSV schon mal in Excel geöffnet, und alles stand in einer Spalte?“ Spezifikationen beseitigen solche Überraschungen.
2. **Test-first + Implementierung (7 Min.)** Prompt 2.2.
3. **Quality Gate (2 Min.)**, `git tag sprint2-fertig`.

### Sprint 3: CLI-Tabelle (8 Min.)
1. **Spezifikation (2 Min.)** Prompt 3.1.
2. **Test-first + Implementierung (4 Min.)** Prompt 3.2.
3. **Vorführen (2 Min.)** `python demo_cli.py`: Tabelle mit fünf Beispielen (zwei/eine/keine Lösung) und CSV-Ausgabe. CSV markieren, in Excel einfügen. `git tag sprint3-fertig`.

### Bonus: Spezifikationsänderung (7 Min.)
Prompt „absteigend sortieren“. Reihenfolge betonen: **SPEC → Tests → Code.** Die Tests schlagen zuerst fehl (neue Regel), dann werden sie grün. Botschaft: Änderungen sind sicher, weil das Gate sofort zeigt, was betroffen ist. Falls die Zeit knapp ist, diesen Block als Erstes streichen.

### Fazit (8 Min.)
1. **Spezifikation** = „Was soll richtig sein?“ (menschliche Aufgabe)
2. **Tests** = „Ist es richtig?“ (maschinell, wiederholbar)
3. **Quality Gate** = „Darf es weiter?“ (automatisch, unbestechlich)

Brücke in den Alltag: Spezifikation, Prüfkriterien und Abnahme funktionieren auch für Excel-Auswertungen, Berichte und Prozesse.
Ehrlich bleiben: KI-Code ist nicht automatisch richtig. **Die Qualität kommt aus den Tests, nicht aus dem Modell.**

## Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| Claude braucht zu lange | Generalprobe mit Stoppuhr. Fallback: Git-Tag. |
| Ergebnis weicht vom Probelauf ab | Das ist ein Feature: Das Gate fängt Abweichungen ab. Offen sagen. |
| Berechtigungsdialoge | Vorab typische Freigaben erlauben (`/fewer-permission-prompts`). Sonst kurz erklären: „Claude fragt, bevor es etwas ausführt.“ |
| Kontext wird lang | `/clear` zwischen den Sprints |
| Netzwerk fällt aus | Hotspot, Screenshots/Video des Probelaufs als Plan C |
| Beamer-Lesbarkeit | Schrift groß, jeweils nur das Wichtige zeigen |

## Checkliste Generalprobe
- [ ] Gesamtdurchlauf mit Stoppuhr
- [ ] Drei Tags gesetzt, Wiederherstellung getestet
- [ ] Mutationsbeispiel geübt (Zeile notiert)
- [ ] Prompts aus PROMPTS.md bereit
- [ ] Anmeldung bei Claude Code und Netzwerk vorher getestet
