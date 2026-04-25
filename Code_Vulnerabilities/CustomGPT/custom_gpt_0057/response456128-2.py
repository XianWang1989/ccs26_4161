
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product directly on 1D arrays (flattened)
r1 = np.outer(X.flatten(), X.flatten())

# Calculate dot product using the transpose of a flattened X
r2 = np.dot(X.flatten(), X.flatten().T)

# Check for equality
result = np.array_equal(r1, r2)

print("r1:")
print(r1)
print("r2:")
print(r2)
print("Are they equal?", result)
