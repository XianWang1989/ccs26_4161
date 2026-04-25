
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer on each pair of rows in X
r1 = np.outer(X, X)  # This will create a much larger tensor, not a 2D array.

# Using np.dot on X and its transpose
r2 = np.dot(X, X.T)  # This gives a 3x3 matrix.

# Check for equality - this will return False because r1 and r2 are different shapes
print(np.array_equal(r1, r2))
