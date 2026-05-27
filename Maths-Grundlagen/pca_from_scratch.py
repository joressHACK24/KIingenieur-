import numpy as np
# Generieren 100 Punkte
x = np.random.normal(0, 1, 100)
# y ist sehr abhängig von x(ein Strarre Zeile)
y = 2 * x + np.random.normal(0, 0.5, 100) 
X = np.c_[x, y] # Mein Datenmatrix 


#Etape 1 : von Jeder Spalte die Mittelwerte von den Werte abziehen
mittelwerte1 = np.mean(X[0])
print(mittelwerte1)

X[0] = X[0] - mittelwerte1

mittelwerte2 = np.mean(X[1])
print(mittelwerte2)

X[1] = X[1] - mittelwerte2


#Etape 2: Die Covarianzmatrix berechnen
n = X.shape[0]
Cov_matrix = (1/n-1)*(X.T@X)


print(Cov_matrix)

#Etape 3: Die eigenvalues und die eigenwerte berechnen

#Methode 1
print("die eigenwerte sind: ", np.linalg.eigvals(Cov_matrix))

#Methode 2
U,S,Vh = np.linalg.svd(Cov_matrix)

y1,y2 = (1/n-1)*np.diag(S**2 )

print(y1,y2)

#Etape 4: Projektieren

Z = X @ U

#oder
y, V = np.linalg.eig(Cov_matrix)

Z_ = X@V

import matplotlib.pyplot as plt

plt.scatter(Z[:, 0], Z[:, 1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Projektierung PCA")
plt

plt.show()