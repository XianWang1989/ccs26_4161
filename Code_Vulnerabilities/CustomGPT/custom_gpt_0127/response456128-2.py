
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to compute a similar result using np.dot
r1 = np.outer(X[0], X[1])  # Compute outer of the first two rows (1D arrays)
r2 = np.dot(X, X.T)  # This will yield a different structure
