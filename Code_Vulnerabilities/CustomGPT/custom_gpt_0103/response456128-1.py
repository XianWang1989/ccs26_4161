
import numpy as np

# Define the matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly compute outer product using np.dot
# Reshape X into vectors
r1 = np.outer(X, np.ones(X.shape[1]))  # Using outer directly
r2 = np.dot(X.T, X)  # Correct calculation

# Check for equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", result)
