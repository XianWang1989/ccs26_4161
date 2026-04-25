
import numpy as np

# Define the matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product using np.outer
r1 = np.outer(X, X)

# Compute a matching result using np.dot
# To match the outer product, you need to flatten X for the outer operation
X_flat = X.flatten()
r2 = np.outer(X_flat, X_flat)  # Get the outer product with flattened array

# Check equality
result = np.array_equal(r1, r2)
print("Do r1 and r2 match?", result)
