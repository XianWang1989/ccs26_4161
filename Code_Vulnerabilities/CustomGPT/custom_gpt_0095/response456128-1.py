
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer with flattened vectors
r1 = np.outer(X.A.ravel(), X.A.ravel())

# Using np.dot with matrix multiplication
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This should print True
