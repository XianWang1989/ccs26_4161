
import numpy as np

X = np.array([1, 5, 4])  # A 1D array representing one vector
Y = np.array([1, 5, 4])  # Another 1D array representing the same vector

# Using np.outer
r1 = np.outer(X, Y)

# Using np.dot to achieve a similar outer product result
r2 = np.dot(X[:, np.newaxis], Y[np.newaxis, :])  # Reshape to 2D

# Check if the results are equal
result = np.array_equal(r1, r2)

print("Outer product using np.outer:\n", r1)
print("Outer product using np.dot:\n", r2)
print("Are they equal? ", result)
