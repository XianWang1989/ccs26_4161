
import numpy as np

# Define the matrix
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product
r2 = np.dot(X.T, X).flatten()

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
