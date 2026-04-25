
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # Outer product: produces a 2D array
r2 = np.dot(X, X.T)  # Dot product (matrix multiplication)

# Check for equality
print(np.array_equal(r1, r2))
