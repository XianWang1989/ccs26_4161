
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correcting the outer product calculation:
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot to mimic the outer product:
# Reshape X to be a 1D vector
r2 = np.dot(X.T, X)

# Check for equality
result = np.array_equal(r1, r2)
print("Arrays are equal:", result)
