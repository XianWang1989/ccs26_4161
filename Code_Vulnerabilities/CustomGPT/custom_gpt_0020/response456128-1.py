
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product of flattened columns (1D arrays)
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product of X and its transpose
r2 = np.dot(X, X.T)

# Check for equality
result = np.array_equal(r1, r2)
print("Do r1 and r2 match?", result)  # This will return True
