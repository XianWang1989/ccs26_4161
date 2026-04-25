
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product for each row vector in X
r1 = np.array([np.outer(X[i, :].A1, X[i, :].A1) for i in range(X.shape[0])])

# Compute the dot product of X and its transpose
r2 = np.dot(X, X.T)

# Check for equality
equal = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", equal)
