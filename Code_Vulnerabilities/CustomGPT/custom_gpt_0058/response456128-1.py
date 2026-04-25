
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to get r1 with np.outer for each row
r1 = np.array([np.outer(row, row) for row in X])

# To achieve the same with np.dot, you can do:
# For matrix X, take the dot product of X with its transpose
r2 = np.dot(X.T, X)

# Check for equality
equal = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?:", equal)
