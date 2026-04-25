
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product using np.outer
r1 = np.outer(X, X)

# To compute the outer product using np.dot, ensure you're working with 1D arrays
r2 = np.dot(X, X.T)  # This will yield a matrix product, not an outer product

# Adjusting r2 for outer product equivalency:
# We use reshaping to flatten X before outer product with itself
r2_adjusted = np.outer(X.flatten(), X.flatten())

# Check equivalency
are_equal = np.array_equal(r1, r2_adjusted)
print(are_equal)  # This should return True
