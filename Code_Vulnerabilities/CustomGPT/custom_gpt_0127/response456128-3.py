
import numpy as np

# Define your matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product of the first two rows
r1 = np.outer(X[0], X[1])

# Matrix multiplication of the full matrix
r2 = np.dot(X, X.T)

# Check for equality
result = np.array_equal(r1, r2)  # This will return True if aligned correctly
print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", result)
