
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product using 1D flattened arrays
r1 = np.outer(X.flatten(), X.flatten())

# To replicate the behavior: we can use np.dot with outer-like structure
r2 = np.dot(X.T, X)  # This computes the dot product on transposed X

# Check equality
are_equal = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", are_equal)  # This should output True
