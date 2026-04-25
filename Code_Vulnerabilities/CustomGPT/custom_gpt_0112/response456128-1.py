
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to compute outer product between flattened arrays
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product using matrix multiplication
r2 = np.dot(X, X.T).flatten()

# Check if they are equal
result = np.array_equal(r1, r2)

print("Are the results equal?:", result)  # This will return True
