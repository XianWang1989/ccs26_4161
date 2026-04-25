
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # This will not work as expected with 2D arrays
r2 = np.dot(X, X.T)  # This computes matrix multiplication
