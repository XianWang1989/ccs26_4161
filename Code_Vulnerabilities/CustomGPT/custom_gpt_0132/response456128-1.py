
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)           # This calculates the outer product.
r2 = np.dot(X, X.T)           # This calculates the dot product (matrix multiplication).
