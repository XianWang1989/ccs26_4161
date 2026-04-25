
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer on each row of X with itself
r1 = np.array([np.outer(X[i], X[i]) for i in range(X.shape[0])])

# Using np.dot, but we need to ensure we only get the outer product
# We can't use np.dot directly on X, as it doesn't yield the correct result.
# Instead, we can flatten X and then reshape to get the required outer product for each row.
r2 = np.array([np.dot(X[i].reshape(-1, 1), X[i].reshape(1, -1)) for i in range(X.shape[0])])

# Check if the arrays are equal
result = np.array_equal(r1, r2)

print("Result of np.array_equal(r1, r2):", result)
