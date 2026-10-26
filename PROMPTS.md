# Prompts zum Kopieren (in dieser Reihenfolge)

Alle Befehle gelten im Demo-Projekt (`quadratic-demo`), nicht in diesem Regiebuch-Repo.

Tipp: Vor jedem Sprint `/clear`. Das Wissen steckt in CLAUDE.md, SPEC.md und im Code.
Das Gate-Ergebnis (✅/❌) soll in Claudes Antwort stehen. Falls nicht: selbst `python check.py` im Terminal ausführen.

## Sprint 1: Backend

**1.1 Spezifikation**
```
Lies CLAUDE.md. Ich möchte die Gleichung x² + p·x + q = 0 lösen. Erstelle eine SPEC.md für Sprint 1 mit: Zweck, Eingaben/Ausgaben, Fallunterscheidung (zwei/eine/keine reelle Lösung), Randfälle und nummerierten Akzeptanzkriterien (AK-1, AK-2 …). Schreibe noch keinen Code. Stelle mir Rückfragen, falls etwas unklar ist.
```

**1.2 Tests zuerst** (vorher prüfen: `ls src/quadratic` zeigt nur `__init__.py`)
```
Schreibe auf Basis der SPEC.md pytest-Tests in tests/, einen pro Akzeptanzkriterium, mit der AK-Nummer im Testnamen. Ergänze einen Test mit vielen Zufallswerten, der die Probe (Einsetzen in die Gleichung) prüft. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
```

**1.3 Implementieren**
```
Implementiere jetzt src/quadratic/solver.py so, dass alle Tests grün werden. Führe danach `python check.py` aus, behebe alle Probleme und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder.
```

**1.4 Sichern (still, ohne Erklärung):** `git add -A && git commit -m "Sprint 1"`. Danach muss `git status --short` leer sein.

**1.5 Mutationstest (manuell):** in solver.py ein Vorzeichen kippen (z. B. `-p / 2` → `+p / 2`), dann `python check.py` → rot. Zurück mit `git checkout src/`.

## Sprint 2: Historie und CSV

**2.1 Spezifikation**
```
Lies CLAUDE.md und SPEC.md. Erweitere SPEC.md um Sprint 2: Ein Modul „History“ nimmt Berechnungen auf (p, q, Anzahl Lösungen, Lösungen, Zeitstempel). Anforderungen: Reihenfolge der Berechnung bleibt erhalten; Funktionen zum Hinzufügen, Abrufen, Leeren; Export als CSV-Text mit Kopfzeile. Entscheide Trennzeichen und Dezimalzeichen sinnvoll für Excel in Deutschland und begründe es kurz in der SPEC. Nummeriere die neuen Akzeptanzkriterien fortlaufend weiter. Noch kein Code.
```

**2.2 Tests zuerst**
```
Schreibe zuerst Tests für Sprint 2 (leere Historie, mehrere Einträge, Fall ohne Lösung, CSV-Format exakt), einen pro Akzeptanzkriterium mit AK-Nummer im Testnamen. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
```

**2.3 Implementieren**
```
Implementiere jetzt die History, bis `python check.py` grün ist, und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder.
```

## Sprint 3: CLI-Tabelle

**3.1 Spezifikation**
```
Lies CLAUDE.md und SPEC.md. Erweitere SPEC.md um Sprint 3: Ein Kommandozeilenprogramm demo_cli.py berechnet fünf feste Beispielgleichungen (mindestens je ein Fall mit zwei, einer und keiner Lösung), legt sie in die History und gibt sie als Tabelle mit ausgerichteten Spalten aus, danach den CSV-Export. Die Tabellenformatierung ist eine eigene, getestete Funktion in src/quadratic/; demo_cli.py im Projektordner ist nur ein dünner Aufruf. Nummeriere die neuen Akzeptanzkriterien fortlaufend weiter. Noch kein Code.
```

**3.2 Tests zuerst**
```
Schreibe zuerst Tests für die Tabellenformatierung (exakter Ausgabetext für ein bis zwei Beispiele), mit AK-Nummer im Testnamen. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
```

**3.3 Implementieren und vorführen**
```
Implementiere jetzt die Tabellenformatierung und demo_cli.py, bis `python check.py` grün ist, und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder. Führe danach `python demo_cli.py` aus.
```

## Bonus: Spezifikationsänderung live

```
Lies CLAUDE.md und SPEC.md. Änderung in der Spezifikation: Lösungen werden absteigend statt aufsteigend sortiert. Gehe in genau dieser Reihenfolge vor: 1. SPEC.md anpassen. 2. Tests anpassen und `python check.py` ausführen; es muss rot sein, zeige das Ergebnis wörtlich. 3. Code anpassen, bis `python check.py` grün ist, und zeige das Endergebnis wörtlich. Fasse am Ende zusammen, was sich geändert hat.
```

## Notfall (nur mit den Tags aus der Generalprobe, im Probe-Ordner)
```
git checkout sprint1-fertig   # bzw. sprint2-fertig / sprint3-fertig
```
