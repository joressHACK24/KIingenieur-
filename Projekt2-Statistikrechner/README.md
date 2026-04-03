# Terminal Stats Calculator

## Projektübersicht
Dieses Projekt ist ein kommandozeilenbasiertes (CLI) Python-Skript zur schnellen statistischen Analyse von CSV-Dateien. Während Jupyter Notebooks ideal für die Exploration sind, demonstriert dieses Projekt die Fähigkeit, produktionsnahen, wiederverwendbaren und robusten Code zu schreiben. 

## Features
* **Automatisierte Berechnungen:** Berechnet sofort Mittelwert (Mean), Median und Varianz für eine ausgewählte Datenspalte.
* **Datenvisualisierung:** Generiert automatisch ein Histogramm und speichert es als `.png`-Datei, ohne eine grafische Benutzeroberfläche zu benötigen.
* **Robustes Error Handling:** Fängt Fehler wie fehlende Dateien oder falsche Datentypen (z.B. Text in numerischen Spalten) sicher ab.

## Tech Stack
* **Python 3** (PEP8 Standard)
* **Pandas / NumPy** (Datenverarbeitung)
* **Matplotlib** (Visualisierung)
* **Argparse / Sys** (CLI-Management)

## Nutzung (Usage)
Um das Skript lokal auszuführen, öffne dein Terminal und nutze folgenden Befehl:

```bash
python calculator.py dein_datensatz.csv -c Spaltenname