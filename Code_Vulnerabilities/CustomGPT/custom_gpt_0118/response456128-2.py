
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten the matrix for outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product with transpose
r2 = np.dot(X, X.T)

# Check for equality
result = np.array_equal(r1, r2)
print("Do r1 and r2 match?", result)  # This should return True
