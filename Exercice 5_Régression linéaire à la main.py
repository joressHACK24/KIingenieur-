import numpy as np
import matplotlib.pyplot as plt

# Taille des maisons (m²) et leur prix (k€)
X_raw = np.array([50, 60, 70, 80, 90, 100])
y     = np.array([150, 180, 210, 230, 270, 300])

# Bereiten wir X vor :
X = np.column_stack((np.ones(len(X_raw)),X_raw))

#wenden wir die normale Gleichung, um w zu finden

X_1 = np.dot(X.T, X)
X_2 = np.dot(X.T, y)
w = np.linalg.solve(X_1, X_2)

print(w)
# machen wir eine Prädiktion von 75 m2

ypred = w[0] + w[1] * 75
print("prediction 75:",ypred)



# Berechnen wir der MSE
ypred = X.dot(w)


MSE = np.mean((ypred - y)**2) 
print("MSE:", MSE)


