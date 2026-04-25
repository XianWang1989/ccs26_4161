import numpy as np

v = np.array([1, 5, 3])
C = np.zeros((v.shape[0], v.max() + 1))
C[np.arange(v.shape[0]), v] = 1
print(C)
