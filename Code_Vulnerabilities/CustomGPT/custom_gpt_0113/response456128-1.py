
import numpy as np

# Define the matrix X
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product using np.outer
r1 = np.outer(X, X)

# Adjust r2 to achieve the outer product effect
r2 = np.einsum('ij,ik->jk', X, X)

# Check for equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
