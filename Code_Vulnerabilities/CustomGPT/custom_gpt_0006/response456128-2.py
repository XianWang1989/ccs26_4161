
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute dot product
r2 = np.dot(X, X.T).flatten()  # Flatten to compare as 1-D

# Check equality
print(np.array_equal(r1, r2))  # This will still return False because they are different shapes.
