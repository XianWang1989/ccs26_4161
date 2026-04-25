
import numpy as np

# Define X as a 2D array
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product
r1 = np.outer(X.flatten(), X.flatten())

# To get a comparable result from dot:
# We need to make X a 1D array first
r2 = np.dot(X.T, X)

# Check if they are the same
result = np.array_equal(r1, r2)
print("Are r1 and r2 equal?", result)  # Should print True
