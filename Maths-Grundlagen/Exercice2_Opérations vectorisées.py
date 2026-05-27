import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#A + B
print(A+B)

#Le produit scalaire (dot product) de A et B
print(np.dot(A,B))

#La multiplication élément par élément de A et B
print(np.multiply(A,B))

'''
           np.dot(A,B)                      np.multiply(A,B)
Nom        Produit matriciel                Produit élément par élément
A[0,0]     1×5 + 2×7 = 19                   1×5 = 5
Règle      Lignes × Colonnes                Même position × Même position
Condition  colonnes de A = lignes de B      A et B de même shape
'''