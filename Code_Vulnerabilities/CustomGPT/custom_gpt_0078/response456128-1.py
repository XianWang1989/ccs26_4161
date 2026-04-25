
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X, X)

# Using np.dot with reshaping
r2 = np.dot(X, X.T)

# Check for equality
equal = np.array_equal(r1, r2)

print("r1 (np.outer):")
print(r1)
print("r2 (np.dot):")
print(r2)
print("Are they equal?", equal)
