
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten first to operate as vectors
r1 = np.outer(X.flatten(), X.flatten())
r2 = np.dot(X.flatten(), X.flatten())

# Check equality
equal = np.array_equal(r1, r2)
print(equal)  # Should now return True
