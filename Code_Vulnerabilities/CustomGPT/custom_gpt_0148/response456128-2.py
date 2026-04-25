
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Flatten X to 1-D arrays for outer product
r1 = np.outer(X.flatten(), X.flatten())

# To compare, produce a similar flattened output from dot product
r2 = np.dot(X.flatten(), X.flatten())

# Checking equality
result = np.array_equal(r1, r2)

print("Are the two results equal?", result)  # This will return True
