
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate using np.outer
r1 = np.outer(X.A.flatten(), X.A.flatten())

# Calculate using np.dot, reshaping appropriately
r2 = np.dot(X.T, X)

# Check for equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", result)
