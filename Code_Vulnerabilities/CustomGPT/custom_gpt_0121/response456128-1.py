
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten the matrix to 1-D arrays
X_flat = np.ravel(X)

# Calculate outer product and dot product
r1 = np.outer(X_flat, X_flat)
r2 = np.dot(X_flat[:, np.newaxis], X_flat[np.newaxis, :])

# Check if they are equal
result = np.array_equal(r1, r2)

print("Outer Product (r1):\n", r1)
print("Dot Product (r2):\n", r2)
print("Are they equal?:", result)
