
import numpy as np

# Define the matrix X
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to calculate outer product using np.dot
# For np.outer, use the flattened version of X
r1 = np.outer(X.flatten(), X.flatten())

# For np.dot, use np.dot(X, X.T) without flattening
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)

print("R1 (using np.outer):\n", r1)
print("R2 (using np.dot):\n", r2)
print("Are they equal? ", result)  # Should return True
