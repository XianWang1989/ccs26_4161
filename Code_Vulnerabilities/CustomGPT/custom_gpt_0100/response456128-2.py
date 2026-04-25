
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Compute equivalent using np.dot
r2 = np.dot(X.flatten().reshape(-1, 1), X.flatten().reshape(1, -1))

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
