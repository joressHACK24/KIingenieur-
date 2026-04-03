import argparse
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Beginn der Statistikrechner")
    # nehme ich die Datei der Nutzer ein
    parser = argparse.ArgumentParser("Lesen der Datei von der Nutzer")
    parser.add_argument("csv_file", help="Pfad zur Datei")
    parser.add_argument('-c','--column',help="Name der Spalte, die wir nutzen wollen") 

    try:
        args = parser.parse_args()
    except FileNotFoundError:
        print("Ihre Datei ist nicht gefunden ")
    except NameError:
        print( " Bitte geben sie ein csv-Datei")


    # muss ich jetzt eine Spalte auswählen und die Mittelwert, Varianz und median rechnen

    Daten = pd.read_csv(args.csv_file, sep=';')

    # wir bewahren nur die Datentyp-Integer
    if Daten[args.column].dtype == "string":
        print("Bitte ändern Sie Ihre Spalte: Sie enhält string-Elemente")
    else:
        Mittelwert = np.mean(Daten[args.column])
        Varianz = np.var(Daten[args.column])
        Median  = np.median(Daten[args.column])

        plt.hist(Daten[args.column])
        plt.savefig(f"hist_{args.column}")
        print(f"Da sind die statistische Komponent der Spalte '{args.column}':\n Mittelwert {Mittelwert},\n Varianz {Varianz},\n Mediane {Median}\n")


if __name__ == "__main__":
    main()

