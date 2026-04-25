
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use np.dot to produce a similar outcome as np.outer
r1 = np.outer(X.flatten(), X.flatten())
r2 = np.dot(X, X.T)  # This computes the dot product of X and its transpose

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1 (outer product):\n", r1)
print("r2 (dot product):\n", r2)
print("Are they equal? ", result)
