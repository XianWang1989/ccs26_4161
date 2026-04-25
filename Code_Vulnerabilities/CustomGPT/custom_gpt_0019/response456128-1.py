
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten the matrix to 1D arrays
x1 = X.flatten()
x2 = X.flatten()

# Perform the outer product
r1 = np.outer(x1, x2)

# Perform the dot product
r2 = np.dot(X, X.T)

# Checking for equality
print(np.array_equal(r1, r2))  # This will return False

# Correctly comparing outer products of flattened vectors
# Consider the outer product of individual rows if needed
outer_results = np.array([np.outer(row.A.flatten(), row.A.flatten()) for row in X])
r1_correct = outer_results.sum(axis=0)

# Compare the accumulated outer products
print(np.array_equal(r1_correct, r2))  # This will return True
