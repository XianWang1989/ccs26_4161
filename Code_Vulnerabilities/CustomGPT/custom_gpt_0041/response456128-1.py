
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculates outer product
r1 = np.outer(X, X)

# Calculates dot product with transpose
r2 = np.dot(X, X.T)
