
import numpy as np

X = np.array([1, 5, 4])  # Vector of shape (3,)
Y = np.array([1, 5, 4])  # Another vector of the same shape

r1 = np.outer(X, Y)      # Outer product
r2 = np.dot(X[:, np.newaxis], Y[np.newaxis, :])  # Reshape to ensure correct dimensions

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", np.array_equal(r1, r2))
