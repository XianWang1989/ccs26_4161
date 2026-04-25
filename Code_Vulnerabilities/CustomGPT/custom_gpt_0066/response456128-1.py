
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product using np.outer
r1 = np.outer(X, X)

# Reshape X to 1-D for outer product
X_flat = X.reshape(-1)

# Calculate using np.dot
r2 = np.dot(X_flat[:, np.newaxis], X_flat[np.newaxis, :])

# Check if they are equal
are_equal = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", are_equal)
