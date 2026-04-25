
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product with 1-D slices
r1 = np.outer(X[0, :], X[1, :])  # Example for first row and second row

# Compare with dot product using transpose
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", result)
