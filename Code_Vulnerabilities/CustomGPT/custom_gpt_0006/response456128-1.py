
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # Computes outer product
r2 = np.dot(X, X.T)  # Computes dot product (matrix multiplication)
print(np.array_equal(r1, r2))  # Returns False
