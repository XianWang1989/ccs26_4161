
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten X for outer product
r1 = np.outer(X.flatten(), X.flatten())
# Perform dot product which yields a different shape
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This will print False
