
import numpy as np

# Using 2D matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product using np.outer (correct usage with 1D arrays)
outer_result = np.outer(X.flatten(), X.flatten())

# Compute the dot product of X and its transpose
dot_result = np.dot(X, X.T)

# Check for equality
are_equal = np.array_equal(outer_result, dot_result)

print("Outer Product using np.outer:\n", outer_result)
print("Dot Product using np.dot:\n", dot_result)
print("Are they equal? ", are_equal)
