import argparse
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# nehme ich die Datei der Nutzer ein
parser = argparse.ArgumentParser("Lesen der Datei von der Nutzer")
parser.add_argument("csv_file", help="Pfad zur Datei")

try:
    args = parser.parse_args()
except FileNotFoundError:
    print("Ihre Datei ist nicht gefunden ")
except NameError:
    print( " Bitte geben sie ein csv-Datei")


# muss ich jetzt eine Spalte auswählen und die Mittelwert, Varianz und median rechnen

Daten = pd.read_csv(args.csv_file, sep=';')



# On garde tout SAUF les colonnes de type 'object'
Daten = Daten.select_dtypes(include=['number'])

print(Daten.head())
for data in Daten.columns:
    Mittelwert = np.mean(Daten[data])
    Varianz = np.var(Daten[data])
    Median  = np.median(Daten[data])

    plt.hist(Daten[data])
    plt.savefig(f"hist_{data}")
    print(f"Da sind die statistische Komponent der Spalte '{data}':\n Mittelwert {Mittelwert},\n Varianz {Varianz},\n Mediane {Median}\n")



