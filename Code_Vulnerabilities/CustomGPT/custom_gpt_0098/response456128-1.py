
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to get an outer product
r1 = np.outer(X.flatten(), X.flatten())

# Change r2 to match the outer product
r2 = np.dot(X.T.flatten(), X.flatten())

# Check if they are equal
result = np.array_equal(r1, r2)

print(result)  # This should return True
