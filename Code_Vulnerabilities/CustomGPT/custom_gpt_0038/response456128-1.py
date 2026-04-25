
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer
r1 = np.outer(X, X)

# To match the outer product using dot, flatten X to 1D
r2 = np.dot(X.flatten()[:, np.newaxis], X.flatten()[np.newaxis, :])

# Check if they are equal
result = np.array_equal(r1, r2)

print(result)  # This should now return True
