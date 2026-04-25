
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using outer product from 1D arrays
r1 = np.outer(X[:, 0], X[:, 1])
r2 = np.dot(X[:, 0].reshape(-1, 1), X[:, 1].reshape(1, -1))  # Properly reshaping for dot product
np.array_equal(r1, r2)  # Now this should return True
