
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product
r1 = np.outer(X, X)

# To get `r2` as an outer product, you need to flatten the matrix
# by taking the first column or row as a vector from X
r2 = np.dot(X, X.T)  # Gives a different shape

# If you want r2 to mimic outer product behavior
# For outer product, compare column vectors
r2 = np.outer(X.flatten(), X.flatten())

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", result)
