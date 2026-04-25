
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct outer product
r1 = np.outer(X.flatten(), X.flatten())

# Using dot product on flattened vectors
r2 = np.dot(X.T, X)

# Check for equality
result = np.array_equal(r1, r2)
print(f"Arrays are equal: {result}")
