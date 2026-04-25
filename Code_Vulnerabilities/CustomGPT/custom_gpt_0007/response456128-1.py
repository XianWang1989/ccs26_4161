
import numpy as np

# Define the matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly use np.outer with 1-D arrays
r1 = np.outer(X.flatten(), X.flatten())

# Use np.dot to get a similar output
r2 = np.dot(X.T, X)

print("r1:\n", r1)
print("r2:\n", r2)

# Check for equality
print(np.array_equal(r1, r2))
