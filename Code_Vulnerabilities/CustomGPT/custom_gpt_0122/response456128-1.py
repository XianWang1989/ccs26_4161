
import numpy as np

# Define the matrix
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# To match the outer product using np.dot, flatten first
r2 = np.dot(X.T, X).A.flatten()

# Check for equality
result = np.array_equal(r1, r2)
print("Are the results equal?", result)
