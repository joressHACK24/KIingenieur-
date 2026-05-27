import numpy as np
probabilites = np.array([0.6, 0.3, 0.1])
gains = np.array([10, 5, 2])


print((np.dot(probabilites,gains)))
