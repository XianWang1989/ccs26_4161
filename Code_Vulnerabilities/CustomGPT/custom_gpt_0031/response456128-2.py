
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product correctly using flattened arrays
r1 = np.outer(X.flatten(), X.flatten())

# Calculate dot product with transpose
r2 = np.dot(X, X.T)

# Check equality
result = np.array_equal(r1, r2)
print(r1)
print(r2)
print("Are r1 and r2 equal? ", result)
