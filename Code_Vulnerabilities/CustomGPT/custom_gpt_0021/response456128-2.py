
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten X for outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute the matrix product of X with its transpose
r2 = np.dot(X.T, X)

# Check equality
result = np.array_equal(r1, r2)
print(result)  # This will print True
