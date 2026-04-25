
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Calculate outer product using np.dot by flattening and reshaping
r2 = np.dot(X, X.T)

# Flatten the matrix for outer product
r2 = r2.flatten()

# Check for equality
result = np.array_equal(r1, r2.reshape(3, 3))
print("Array equal:", result)
