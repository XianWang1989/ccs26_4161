
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product correctly by flattening the matrix
r1 = np.outer(X.flatten(), X.flatten())

# To match dimensions, use np.einsum or reshape
r2 = np.einsum('ij,ik->jk', X, X)

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This should print True
