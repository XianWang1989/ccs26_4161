
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X, X)

# Using np.dot with flattened 1-D arrays
r2 = np.dot(X.T, X)

# Check equality
result = np.array_equal(r1, r2)

print("Outer product (r1):\n", r1)
print("Dot product (r2):\n", r2)
print("Are they equal?", result)
