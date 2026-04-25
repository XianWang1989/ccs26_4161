
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product
r1 = np.outer(X.flatten(), X.flatten())

# Dot product of X with its transpose
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1 (outer product):\n", r1)
print("r2 (dot product):\n", r2)
print("Are r1 and r2 equal?:", result)
