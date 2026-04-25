
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product for the first column vector
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product of X and its transpose
# This effectively gives a matrix, but not an equivalent outer product
r2 = np.dot(X, X.T)

# Check equality (this will be False)
are_equal = np.array_equal(r1, r2)

print("r1 (outer product):\n", r1)
print("r2 (dot product):\n", r2)
print("Are they equal?", are_equal)
