
import numpy as np

# Define the matrix
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product correctly using 1-D flattened arrays
r1 = np.outer(X.flatten(), X.flatten())

# Correctly computing the outer product to match `np.outer`
r2 = np.dot(X.T.flatten(), X.flatten())

# Check if they are equal
equal_result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?:", equal_result)
