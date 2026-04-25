
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# r1 as outer product
r1 = np.outer(X.flatten(), X.flatten())

# r2 as a reshaped dot product
r2 = np.dot(X, X.T).flatten()

# Check equality
equal_result = np.array_equal(r1, r2)
print(equal_result)  # Should return True
