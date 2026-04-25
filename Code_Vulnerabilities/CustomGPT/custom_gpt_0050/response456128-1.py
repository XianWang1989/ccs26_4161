
import numpy as np

# Convert to 1-D arrays
X = np.array([1, 5, 4])  # Choose one of the rows/columns

# Compute outer product
r1 = np.outer(X, X)

# Compute dot product
r2 = np.dot(X.reshape(-1, 1), X.reshape(1, -1))  # Reshape to 2D for proper outer product

# Check equality
result = np.array_equal(r1, r2)
print("Are r1 and r2 equal?", result)
