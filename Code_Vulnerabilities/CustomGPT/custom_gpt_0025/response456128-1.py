
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product
r1 = np.outer(X.ravel(), X.ravel())

# Calculate dot product
r2 = np.dot(X, X.T)

# Check for equality
result = np.array_equal(r1, r2)
print(result)  # This should return True
