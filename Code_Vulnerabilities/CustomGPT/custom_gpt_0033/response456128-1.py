
import numpy as np

# Original matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use 1-D arrays for outer product
r1 = np.outer(X.ravel(), X.ravel())

# Perform dot product with the first axis correctly set up
r2 = np.dot(X.T.ravel(), X.ravel())

# Check for equality
equal = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", equal)
