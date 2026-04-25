
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to calculate the outer product
r1 = np.outer(X.flatten(), X.flatten())
# Using np.dot to compute outer-like product using flatten()
r2 = np.dot(X.T.flatten(), X.flatten())

# Check for equality
result = np.array_equal(r1, r2)
print(result)  # This should return True
