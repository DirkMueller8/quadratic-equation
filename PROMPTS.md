# Prompts zum Kopieren (in dieser Reihenfolge)

Alle Befehle gelten im Demo-Projekt (`quadratic-demo`), nicht in diesem Regiebuch-Repo.

Tipp: Vor jedem Sprint `/clear`. Das Wissen steckt in CLAUDE.md und SPEC.md.

## Sprint 1: Backend

**1.1 Spezifikation**
```
Lies CLAUDE.md. Ich möchte die Gleichung x² + p·x + q = 0 lösen. Erstelle eine SPEC.md für Sprint 1 mit: Zweck, Eingaben/Ausgaben, Fallunterscheidung (zwei/eine/keine reelle Lösung), Randfälle und nummerierten Akzeptanzkriterien (AK-1, AK-2 …). Schreibe noch keinen Code. Stelle mir Rückfragen, falls etwas unklar ist.
```

**1.2 Tests zuerst**
```
Schreibe auf Basis der SPEC.md pytest-Tests in tests/, einen pro Akzeptanzkriterium, mit der AK-Nummer im Testnamen. Ergänze einen Test mit vielen Zufallswerten, der die Probe (Einsetzen in die Gleichung) prüft. Implementiere noch nichts. Führe `python check.py` aus und gib das Ergebnis wörtlich in deiner Antwort wieder; es muss rot sein.
```

**1.3 Implementieren**
```
Implementiere jetzt src/quadratic/solver.py so, dass alle Tests grün werden. Führe danach `python check.py` aus, behebe alle Probleme und gib das Endergebnis des Gates wörtlich in deiner Antwort wieder.
```

**1.5 Mutationstest (manuell):** in solver.py ein Vorzeichen kippen (z. B. `-p / 2` → `+p / 2`), dann `python check.py` → rot. Zurück mit `git checkout src/`.

## Sprint 2: Historie und CSV

**2.1 Spezifikation**
```
Erweitere SPEC.md um Sprint 2: Ein Modul „History“ nimmt Berechnungen auf (p, q, Anzahl Lösungen, Lösungen, Zeitstempel). Anforderungen: Reihenfolge der Berechnung bleibt erhalten; Funktionen zum Hinzufügen, Abrufen, Leeren; Export als CSV-Text mit Kopfzeile. Entscheide Trennzeichen und Dezimalzeichen sinnvoll für Excel in Deutschland und begründe es kurz in der SPEC. Noch kein Code.
```

**2.2 Test-first und Implementierung**
```
Schreibe zuerst Tests für Sprint 2 (leere Historie, mehrere Einträge, Fall ohne Lösung, CSV-Format exakt). Zeige, dass sie rot sind. Implementiere dann, bis `python check.py` grün ist.
```

## Sprint 3: CLI-Tabelle

**3.1 Spezifikation**
```
Erweitere SPEC.md um Sprint 3: Ein Kommandozeilenprogramm demo_cli.py berechnet fünf feste Beispielgleichungen (mindestens je ein Fall mit zwei, einer und keiner Lösung), legt sie in die History und gibt sie als Tabelle mit ausgerichteten Spalten aus, danach den CSV-Export. Die Tabellenformatierung ist eine eigene, getestete Funktion. Noch kein Code.
```

**3.2 Test-first und Implementierung**
```
Schreibe zuerst Tests für die Tabellenformatierung (exakter Ausgabetext für ein bis zwei Beispiele), dann die Implementierung und demo_cli.py, bis `python check.py` grün ist. Führe danach demo_cli.py aus.
```

## Bonus: Spezifikationsänderung live

```
Änderung in der Spezifikation: Lösungen werden absteigend statt aufsteigend sortiert. Gehe in der richtigen Reihenfolge vor: erst SPEC.md anpassen, dann die Tests, dann den Code, bis `python check.py` grün ist. Fasse am Ende zusammen, was sich geändert hat.
```

## Notfall
```
git checkout sprint1-fertig   # bzw. sprint2-fertig / sprint3-fertig
```
