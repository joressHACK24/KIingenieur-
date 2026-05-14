# Ich habe das Video von Gilbert Strang über SVD angeschaut und ich habe viele Sache gelernt.
# Jetzt muss ich diese Theorie Fachbegriffe im Pratik setzen

import numpy as np
Matrix_lambda = np.arange(1,17).reshape(4,4)
print(Matrix_lambda)

print(np.linalg.svd(Matrix_lambda))


#Zweie Etape: Die Lösung überprüfen...

U, S, Vh = np.linalg.svd(Matrix_lambda)


print("Die Matrix von dem Beginnn ist:")

A = U@np.diag(S)@Vh
print(A)