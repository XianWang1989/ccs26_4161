
import numpy as np

# Your matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flattening the matrix to 1D arrays (vectors)
X1 = X[0]  # First row as vector
X2 = X[1]  # Second row as vector

# Using np.outer to compute outer product
r1 = np.outer(X1, X2)  # Change this for whichever vectors you want

# Using np.dot for matrix multiplication
r2 = np.dot(X1.reshape(-1, 1), X2.reshape(1, -1))

# Check for equality
print(np.array_equal(r1, r2))  # This should return True
