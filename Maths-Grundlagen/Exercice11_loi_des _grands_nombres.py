import numpy as np
import matplotlib.pyplot as plt

# Simulieren wir aufeinanderfolgende Münzwürfe
Größen = [10, 100, 1000, 10000, 100000]

for n in Größen:
    Würfe = np.random.binomial(n=1, p=0.5, size=n)
    mittelwert = np.mean(Würfe)
    print(f"n={n} → mittelwert = {mittelwert:.4f}")


# Betrachten wir die Konvergenz der Mittelwerte nach 1000 Würfen    
Würfe = np.random.binomial(n=1, p=0.5, size=1000)
kumulierte_mittelwerte = np.cumsum(Würfe) / np.arange(1, 1001)
plt.plot(kumulierte_mittelwerte)
plt.axhline(y=0.5, color='r', linestyle='--')
plt.show()