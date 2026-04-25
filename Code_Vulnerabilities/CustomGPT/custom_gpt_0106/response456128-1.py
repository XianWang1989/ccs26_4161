
import numpy as np

# Define the matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product using np.outer
r1 = np.outer(X, X)

# Calculate using np.dot on the transposed version
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1 (outer product):\n", r1)
print("r2 (dot product):\n", r2)
print("Are they equal?:", result)
