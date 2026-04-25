
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # Outputs a 3D result (outer product of each pair)
r2 = np.dot(X, X.T)  # Matrix multiplication (result is 3x3)
result = np.array_equal(r1, r2)  # Returns False
