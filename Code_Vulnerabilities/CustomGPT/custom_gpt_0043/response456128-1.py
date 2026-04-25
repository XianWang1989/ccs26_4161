
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use np.outer as is
r1 = np.outer(X.flat, X.flat)

# Flatten X into 1D arrays for the dot product
r2 = np.dot(X.flat, X.flat.T)

# Check if they are equal
result = np.array_equal(r1, r2)
print("Are r1 and r2 equal? ", result)
