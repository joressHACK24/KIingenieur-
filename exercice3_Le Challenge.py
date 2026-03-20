
# Sans utiliser @ ni np.dot, écris une fonction Python avec des boucles for qui multiplie deux matrices :
import numpy as np


def multiply_matrices(A, B):
    

    ligne_A = A.shape[0]
    colonne_B = B.shape[1]
    C = np.zeros((ligne_A, colonne_B))
    for i in range(ligne_A):
        for j in range(colonne_B):
                C[i][j] = np.sum(A[i,:]*B[:,j])
'''   
    def multiply_matrices(A, B):
    lignes_A = A.shape[0]
    colonnes_B = B.shape[1]
    colonnes_A = A.shape[1]

    C = np.zeros((lignes_A, colonnes_B))

    for i in range(lignes_A):
        for j in range(colonnes_B):
            for k in range(colonnes_A):
                C[i][j] += A[i][k] * B[k][j]  # ✅
    return C

# Vérification
print(multiply_matrices(A, B))
print(np.dot(A, B))  # Doit donner le même résultat
    return C
'''
A = np.array([[1, 2, 3], [4, 5, 6]])        # shape (2, 3)
B = np.array([[7, 8], [9, 10], [11, 12]])   # shape (3, 2)

result = multiply_matrices(A, B)
print(result)
# Résultat attendu :
# [[ 58  64]
#  [139 154]]