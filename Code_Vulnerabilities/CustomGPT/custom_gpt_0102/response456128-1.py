
import numpy as np

# Define a 1D array
X = np.array([1, 5, 4])  # Example: 1D array

# Calculate using np.outer
r1 = np.outer(X, X)

# Calculate using np.dot (reshaping to 2D)
r2 = np.dot(X[:, np.newaxis], X[np.newaxis, :])

# Check equality
result = np.array_equal(r1, r2)

print("r1 (outer product):\n", r1)
print("r2 (dot product):\n", r2)
print("Are they equal?", result)
