
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use outer product correctly
r1 = np.outer(X.flatten(), X.flatten())  # Flatten to make outer product

# Reshape for comparison
r2 = np.dot(X.T, X)  # Matrix multiplication

# Check if they are equal
print(np.array_equal(r1, r2))  # Adjust as needed to align shapes
