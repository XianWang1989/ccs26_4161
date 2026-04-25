
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to use np.outer with 1D vectors
r1 = np.outer(X.flatten(), X.flatten())

# Use np.dot correctly (dot product on reshaped arrays)
r2 = np.dot(X.T, X)

# Check equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
