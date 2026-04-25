
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten the matrix to 1D arrays
X_flat = X.flatten()

# Calculate the outer product
r1 = np.outer(X_flat, X_flat)

# Calculate the dot product with the transpose, ensuring correct shape
r2 = np.dot(X_flat[:, np.newaxis], X_flat[np.newaxis, :])  # This creates a 2D array like outer product

# Check if they are equal
result = np.array_equal(r1, r2)

print("Are the results equal:", result)
