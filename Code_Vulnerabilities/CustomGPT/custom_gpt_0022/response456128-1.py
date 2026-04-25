
import numpy as np

# Define your matrix as a 2D array (not a matrix object)
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute `np.outer` on flattened arrays
r1 = np.outer(X.flatten(), X.flatten())

# Compute dot product of X and its transpose
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # Should print True
