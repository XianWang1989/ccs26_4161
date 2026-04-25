
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product manually
r1 = np.outer(X.flatten(), X.flatten())

# Compute dot product with the appropriate dimensions
r2 = np.dot(X.T, X)

# Check if the results are equal
result = np.array_equal(r1, r2)
print("Are r1 and r2 equal?", result)
