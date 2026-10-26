# Prompts zum Kopieren (in dieser Reihenfolge)

Alle Befehle gelten im Demo-Projekt (`quadratic-demo`), nicht in diesem Regiebuch-Repo.

Tipp: Vor Sprint 2 `/clear`. Das Wissen steckt in CLAUDE.md, SPEC.md und im Code.
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
Implementiere jetzt den Code, bis alle Tests grün werden. Führe danach `python check.py` aus, behebe alle Probleme und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder.
```

**1.4 Sichern (still, ohne Erklärung):** `git add -A && git commit -m "Sprint 1"`. Danach muss `git status --short` leer sein.

**1.5 Mutationstest (manuell, in der IDE):** in der Lösungsformel ein Vorzeichen kippen (z. B. `-p / 2` → `+p / 2`), speichern, dann selbst im Terminal `python check.py` → rot. Zurück mit `git checkout src/` und Gate noch einmal ausführen → grün.

## Sprint 2: Ergebnis als CSV

**2.1 Spezifikation**
```
Lies CLAUDE.md und SPEC.md. Erweitere SPEC.md um Sprint 2: Das Ergebnis einer einzelnen Berechnung (p, q und die Lösungen) soll als CSV-Text ausgegeben werden können: eine Kopfzeile und genau eine Datenzeile. Keine Historie, keine Datei, nur Text. Entscheide Trennzeichen und Dezimalzeichen sinnvoll für Excel in Deutschland und begründe es kurz in der SPEC. Lege fest, wie die Fälle mit einer und mit keiner Lösung dargestellt werden. Nummeriere die neuen Akzeptanzkriterien fortlaufend weiter. Noch kein Code.
```

**2.2 Tests zuerst**
```
Schreibe zuerst Tests für Sprint 2 (zwei Lösungen, eine Lösung, keine Lösung, CSV-Text exakt), einen pro Akzeptanzkriterium mit AK-Nummer im Testnamen. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
```

**2.3 Implementieren**
```
Implementiere jetzt den CSV-Export, bis `python check.py` grün ist, und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder.
```

**2.4 Vorführen**
```
Berechne p = -3 und q = 2 und gib den CSV-Text im Terminal aus. Danach dasselbe für p = 0 und q = 1.
```
Den CSV-Text markieren, in Excel (oder Notepad) einfügen.

## Notfall (nur mit den Tags aus der Generalprobe, im Probe-Ordner)
```
git checkout sprint1-fertig   # bzw. sprint2-fertig
```
