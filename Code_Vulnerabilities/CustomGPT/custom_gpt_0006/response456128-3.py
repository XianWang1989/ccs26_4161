
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# For r2, matrix multiplication of the columns
r2 = np.matmul(X.T, X)

print(np.array_equal(r1, r2))  # This should return False.
