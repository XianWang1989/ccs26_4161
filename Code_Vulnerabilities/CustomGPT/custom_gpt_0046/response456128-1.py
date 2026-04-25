
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X.ravel(), X.ravel())

# Using np.dot
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1 (outer product):")
print(r1)
print("r2 (dot product):")
print(r2)
print("Are they equal?", result)
