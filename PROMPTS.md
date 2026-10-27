# Prompts zum Kopieren (in dieser Reihenfolge)

Alle Befehle gelten im Demo-Projekt (`quadratic-demo`), nicht in diesem Regiebuch-Repo.

Tipp: Vor Sprint 2 `/clear`. Das Wissen steckt in CLAUDE.md, SPEC.md und im Code.
Das Gate-Ergebnis (✅/❌) soll in Claudes Antwort stehen. Falls nicht: selbst `python check.py` im Terminal ausführen.

## Sprint 1: Backend

**1.1 Spezifikation**
```
Lies CLAUDE.md. Ich möchte die Gleichung x² + p·x + q = 0 lösen. Erstelle eine SPEC.md für Sprint 1 mit: Zweck, Eingaben/Ausgaben, Fallunterscheidung (zwei/eine/keine reelle Lösung). Ignoriere Randfälle wie sehr kleine oder sehr grosse Zahlen in Input oder Output, oder leeren Input. Nummeriere die Fälle und errichte Akzeptanzkriterien (AK-1, AK-2 …). Schreibe noch keinen Code. Stelle mir Rückfragen, falls etwas unklar ist.
```

**1.2 Tests zuerst** (vorher prüfen: `ls src/quadratic` zeigt nur `__init__.py`)
```
Schreibe auf Basis der SPEC.md pytest-Tests in tests/, einen pro Akzeptanzkriterium, mit der AK-Nummer im Testnamen. Ergänze einen Test mit einigen Zufallswerten, der die Probe (Einsetzen in die Gleichung) prüft. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
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
Lies CLAUDE.md und SPEC.md. Erweitere SPEC.md um Sprint 2: Jede Berechnung wird in die Datei ergebnis.csv im Projektordner geschrieben. Die Kopfzeile steht genau einmal oben, danach kommt pro Berechnung eine Zeile mit Eingabe (p, q) und Ausgabe (Anzahl Lösungen, x1, x2). Neue Zeilen werden nacheinander angehängt, nie überschrieben. Die Berechnungen kommen entweder aus den Testfällen oder aus einer manuellen Eingabe von p und q im Terminal; beides schreibt in dieselbe Datei. Entscheide Trennzeichen und Dezimalzeichen sinnvoll für Excel in Deutschland und begründe es kurz in der SPEC. Lege fest, wie Fälle mit einer und keiner Lösung dargestellt werden (fehlende Werte leer). Nummeriere die neuen Akzeptanzkriterien fortlaufend weiter. Noch kein Code.
```

**2.2 Tests zuerst**
```
Schreibe zuerst Tests für Sprint 2 (Datei wird mit Kopfzeile angelegt, mehrere Zeilen werden in Reihenfolge angehängt, zwei Lösungen, eine Lösung, keine Lösung, Dateiinhalt exakt). Die Tests nutzen ein temporäres Verzeichnis, nicht den Projektordner. Ein Test pro Akzeptanzkriterium mit AK-Nummer im Testnamen. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
```

**2.3 Implementieren**
```
Implementiere jetzt das Anhängen an ergebnis.csv und die manuelle Eingabe: Ein kleines Startskript im Projektordner fragt im Terminal nach p und q, berechnet, zeigt das Ergebnis und hängt es an die Datei an. Bis `python check.py` grün ist, und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder. Nenne mir am Ende, wie das Skript gestartet wird.
```

**2.4 Vorführen**
```
Schreibe die Testfälle p = -3, q = 2 und p = 0, q = 1 mit Eingabe und Ausgabe in ergebnis.csv. Danach gib manuell p = 2 und q = 1 im Terminal ein. Zeige am Ende den Inhalt von ergebnis.csv im Terminal.
```
