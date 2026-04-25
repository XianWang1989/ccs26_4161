
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use outer product
r1 = np.outer(X, X)

# Use dot product with flattened arrays
r2 = np.dot(X.flatten(), X.flatten())

# Check if they are equal
print(np.array_equal(r1, r2.reshape(r1.shape)))  # This will be False
