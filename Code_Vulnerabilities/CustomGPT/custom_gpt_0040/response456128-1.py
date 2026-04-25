
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer with reshaping
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot with reshaping to 1-D arrays
r2 = np.dot(X.flatten(), X.flatten()[None, :])

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
