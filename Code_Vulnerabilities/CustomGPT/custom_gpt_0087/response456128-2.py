
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot on flattened version
r2 = np.dot(X.flatten(), X.flatten().T)

# Check if they are equal
print(np.array_equal(r1, r2))  # This should now return True
