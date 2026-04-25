
import numpy as np

# Provide one-dimensional arrays
a = np.array([1, 5, 4])
b = np.array([1, 5, 4])

# Compute outer product using np.outer
r1 = np.outer(a, b)  # This produces a (3, 3) array.

# Compute dot product of the column vector with its transpose
r2 = np.dot(a.reshape(-1, 1), b.reshape(1, -1))

# Check for equality
result = np.array_equal(r1, r2)
print(result)  # This will print True.
