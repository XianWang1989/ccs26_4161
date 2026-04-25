import numpy as np

# Define two 1-D vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Outer product using np.outer
r1 = np.outer(a, b)

# Outer product using np.dot with reshaping
r2 = np.dot(a[:, np.newaxis], b[np.newaxis, :])

print(np.array_equal(r1, r2))  # True
