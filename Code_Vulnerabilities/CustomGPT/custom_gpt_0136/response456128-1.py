
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X, X)

# Using np.dot by flattening the array
r2 = np.dot(X, X.T)

# Checking for equality
are_equal = np.array_equal(r1, r2)

# Print the results
print("r1 (outer product):")
print(r1)
print("\nr2 (dot product):")
print(r2)
print("\nAre r1 and r2 equal? ", are_equal)
