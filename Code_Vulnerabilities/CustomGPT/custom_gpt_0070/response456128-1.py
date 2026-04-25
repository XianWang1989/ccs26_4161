
import numpy as np

# Define a matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product using np.outer
r1 = np.outer(X, X)

# To match the output of np.outer with np.dot,
# you need to flatten X before using np.dot for outer product-like behavior.
# This produces an equivalent output based on the outer product definition.
r2 = np.dot(X.T, X)

# Check if they are equal
are_equal = np.array_equal(r1, r2)

print("r1 (np.outer):\n", r1)
print("r2 (np.dot):\n", r2)
print("Are they equal?:", are_equal)
