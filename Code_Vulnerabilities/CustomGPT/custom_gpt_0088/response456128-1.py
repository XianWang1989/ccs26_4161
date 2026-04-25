
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct use of np.outer
r1 = np.outer(X, X)

# Using np.dot to mimic outer product
r2 = np.empty((X.shape[0], X.shape[0]))
for i in range(X.shape[0]):
    r2[i] = np.dot(X[i, :].A1, X[i, :].A1)

# Check if they are equal
result = np.array_equal(r1, r2)

print("Are r1 and r2 equal?", result)
