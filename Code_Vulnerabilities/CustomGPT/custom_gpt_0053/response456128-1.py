
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # This does not behave as expected
r2 = np.dot(X, X.T)  # This computes matrix multiplication
np.array_equal(r1, r2)  # This will return False
