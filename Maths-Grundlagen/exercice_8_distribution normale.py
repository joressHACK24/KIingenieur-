import numpy as np
import matplotlib.pyplot as plt

# Génère 1000 points avec moyenne=0, écart-type=1
data = np.random.normal(loc=0, scale=1, size=1000)

print(data)

# prüfen wir, dass Durchschnitt = 0  und varianz = 1

Durchschnitt = np.mean(data)

print("Durchschnitt:", Durchschnitt)

Standardabweichung = (np.var(data))**0.5

print("die Standardabweichung:",Standardabweichung)

#Beobactung = Die daten sind fast gleich

#wie viel prozent von Daten sind in diesem Abstand [-1, 1]

# zähler wir punkte zwischen -1 und 1
in_Abstand = np.sum((data >= -1) & (data <= 1))
Prozentsatz = (in_Abstand / len(data)) * 100
print(f"{Prozentsatz:.1f}% der Daten sind in [-1, 1]")


# zeichen wir das Histogramm
plt.hist(data, bins= 30)
plt.show()