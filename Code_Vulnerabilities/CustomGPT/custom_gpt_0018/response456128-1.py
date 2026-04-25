
import numpy as np

# Define your matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use a single vector for outer product
r1 = np.outer(X.flatten(), X.flatten())

# For r2, we need to use the relevant reshaping
r2 = np.dot(X.flatten().reshape(-1, 1), X.flatten().reshape(1, -1))

# Check if they are equal
result = np.array_equal(r1, r2)
print("Are r1 and r2 equal? :", result)  # This will return True
