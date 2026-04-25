
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product
r1 = np.outer(X.ravel(), X.ravel())

# Calculate dot product and reshape appropriately
r2 = np.dot(X.T, X)

# Check if they are equal
equal = np.array_equal(r1, r2)

print("r1 (outer):\n", r1)
print("r2 (dot):\n", r2)
print("Are they equal?", equal)
