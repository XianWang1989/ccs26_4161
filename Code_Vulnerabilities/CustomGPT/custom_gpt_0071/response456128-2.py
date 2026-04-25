
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product
r1 = np.outer(X.flatten(), X.flatten())

# Calculate the dot product of original and its transpose
r2 = np.dot(X.flatten(), X.flatten())

# Check for equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
