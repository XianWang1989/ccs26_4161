
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer with a flattened version of X
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot on X with its transpose
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)

print(result)  # This should print True
