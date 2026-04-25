
import numpy as np

# Define a 2D matrix
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# To produce a similar result with np.dot, 
# we first need to ensure we flatten X properly
# and we need to compute the outer product for each unique row
# Here's an alternative using np.dot:
r2 = np.dot(X.T, X)

# Check if the results are equal
are_equal = np.array_equal(r1, r2)
print(f"Are the results equal? {are_equal}")

# Print both results
print("Using np.outer:\n", r1)
print("Using np.dot:\n", r2)
