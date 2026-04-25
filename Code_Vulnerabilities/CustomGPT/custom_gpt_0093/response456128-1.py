
import numpy as np

# Define a matrix X
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly compute the outer product
r1 = np.outer(X[0], X[0])  # Example for the first row
r2 = np.dot(X[0].reshape(-1, 1), X[0].reshape(1, -1))  # Row vector to column vector

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", result)
