
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # Outer product of the matrix flattened
r2 = np.dot(X, X.T)  # Matrix multiplication of X with its transpose
