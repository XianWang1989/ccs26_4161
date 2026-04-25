
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer products for each row
r1 = np.array([np.outer(X[i].A1, X[i].A1) for i in range(X.shape[0])])

# Calculate dot products
r2 = np.dot(X, X.T)

# Verify equality
equal = np.array_equal(r1, r2)

print("Are they equal?", equal)
