
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product
r1 = np.outer(X, X)

# Calculate the dot product with reshaping
# This simulates the outer product by manually reshaping
r2 = np.dot(X.T, X).flatten()

# Check if they are equal
result = np.array_equal(r1, r2)
print("Are they equal?", result)
