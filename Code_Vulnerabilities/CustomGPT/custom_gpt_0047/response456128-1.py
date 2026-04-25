
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product
r1 = np.outer(X, X)

# Reshape and calculate the dot product
# We need to flatten X to 1D vectors for the outer product
X_flat = X.flatten()
# Adjust for correct shape
r2 = np.dot(X_flat[:, np.newaxis], X_flat[np.newaxis, :])

# Check if they are equal
result = np.array_equal(r1, r2)

print("Are the results equal?", result)
