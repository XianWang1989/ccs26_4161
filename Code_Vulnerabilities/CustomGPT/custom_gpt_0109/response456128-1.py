
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot with flattened input
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1 (outer product):")
print(r1)
print("\nr2 (matrix multiplication):")
print(r2)
print("\nAre they equal?:", result)
