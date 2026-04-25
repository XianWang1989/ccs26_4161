
import numpy as np

# Define the matrix
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product using np.outer
r1 = np.outer(X.A.flatten(), X.A.flatten())

# Dot product using np.dot
# Use the transpose of X for the dot product
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1 (np.outer):\n", r1)
print("r2 (np.dot):\n", r2)
print("Are they equal?:", result)  # This will print False
