import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Download latest version
path = kagglehub.dataset_download("yasserh/titanic-dataset")

print("Path to dataset files:", path)

dataset_titanik = pd.read_csv("C:/Users/jores/.cache/kagglehub/datasets/yasserh/titanic-dataset/versions/1/Titanic-Dataset.csv")

#print(dataset_titanik.head())

# da würde ich gern wissen, welche Columns gibt es in der Dataset

print(dataset_titanik.describe())
# Mit diesen Analyse weiß ich jetzt, dass es Alter von anderer Leute fehlt.
# jetzt habe ich den Wahl zwischen die löschung von "N/a" Daten oder ich ersetze mit dem Median
# ich habe mich entschieden , die fehlende Daten zu löschen
# und eine Andere Spalte zu erstellen( name : verwandte( EN: Relative))
print(dataset_titanik["Survived"].value_counts(normalize=True))
dataset_titanik["Relative"] = dataset_titanik["SibSp"] + dataset_titanik["Parch"]

dataset_titanik_clean = dataset_titanik.dropna(subset=["Age"])
print(dataset_titanik_clean["Survived"].value_counts(normalize=True))
# Die Rate von "survived" ist um 2% gestiegen , nachdem ich die fehlende Alter gelöscht habe.

# jetzt habe ich eine Analyse gemacht : würde ich die Geschlecht, und die Klasse der Fahrgäste, von denen
# die Altengruppen nicht registriert werden
print(dataset_titanik[dataset_titanik["Age"].isna()].groupby(["Sex", "Pclass"]).size())
# sex       Pclass      count
# W         1           9
#           2           2
#           3           42
# ---------------------------------
# M         1           21
#           2           9
#           3           94

# Abschließnd würde ich sagen, dass die Dataset fehlen die Altergruppen von Leuten, die in Klasse 3
# waren.( insbesonderes Männer) und auch Männer von Klasse 1. 

# Wie diese Daten die Rate von überlebenden erhöhen haben , könnten wir sagen, dass viele männer von Klasse 3, die wir
# der Alter nicht wissen , hatten nicht überleben.
print(dataset_titanik_clean["Cabin"].head())



