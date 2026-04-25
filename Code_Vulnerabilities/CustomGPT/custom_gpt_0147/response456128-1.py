
import numpy as np

# Define matrix X
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product by choosing appropriate vectors
r1 = np.outer(X.flatten(), X.flatten())

# Compute the dot product by reshaping or flipping the original matrix
r2 = np.dot(X, X.T).flatten()  # or simply use np.sum(X * X.T, axis=1)

# Check if arrays are equal (it won't be unless we directly compare flattened shapes)
are_equal = np.array_equal(r1, r2)

print("Are the two results equal?:", are_equal)
print("Outer product:\n", r1)
print("Dot product result:\n", r2)
