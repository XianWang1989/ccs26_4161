
import numpy as np

# Define the matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product
r1 = np.outer(X.flatten(), X.flatten())

# Calculate the dot product (matrix multiplication)
r2 = np.dot(X.T, X)

# Check equality
result = np.array_equal(r1, r2)
print(result)
