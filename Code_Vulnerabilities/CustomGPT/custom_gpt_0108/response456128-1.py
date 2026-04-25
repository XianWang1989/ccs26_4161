
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Calculate the outer product using np.dot by reshaping
r2 = np.dot(X.T.flatten(), X.flatten()).reshape(X.shape[1], X.shape[0], X.shape[1], X.shape[0]).sum(axis=(0, 2))

# Check if they are equal
are_equal = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", are_equal)
