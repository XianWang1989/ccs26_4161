
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use np.dot with reshaping
r1 = np.outer(X.flatten(), X.flatten())
r2 = np.dot(X.T, X)  # This reflects the outer product for 2D arrays
result = np.array_equal(r1, r2)

print(result)  # Should return True
