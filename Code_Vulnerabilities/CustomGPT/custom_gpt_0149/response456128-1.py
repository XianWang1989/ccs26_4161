
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product
r1 = np.outer(X.flatten(), X.flatten())  # Flatten to treat as vectors

# Compute dot product of X with its transpose
r2 = np.dot(X, X.T)

# Check equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", result)
