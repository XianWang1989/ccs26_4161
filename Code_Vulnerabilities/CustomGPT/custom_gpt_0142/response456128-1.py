
import numpy as np

# Define the matrix X
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product such that it resembles the outer product
r2 = np.dot(X.T, X)  # Transpose X and then dot with X

# Check if the two outputs are equal
print(np.array_equal(r1, r2))
