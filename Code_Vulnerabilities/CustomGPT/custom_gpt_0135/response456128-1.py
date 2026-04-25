
import numpy as np

# Define the matrix X
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product using np.outer
r1 = np.outer(X, X)  # Resulting in a 3D array

# To get equivalent product with np.dot, use np.dot with reshaping
# This reshapes X to 1D column and 1D row for outer product
r2 = np.dot(X.T, X)  # Check for dimensions

# Compare results
result = np.array_equal(r1, r2)  # This will be False because shapes mismatch
print("Are the results equal?", result)  # Output: False
