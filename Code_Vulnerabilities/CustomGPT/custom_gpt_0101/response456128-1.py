
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Converting to 1D arrays for outer product
r1 = np.outer(X.A1, X.A1)  # Use .A1 to flatten to 1D
r2 = np.dot(X, X.T)

# To compare outer products for each row
r2_correct = np.array([np.outer(X[i].A1, X[i].A1) for i in range(X.shape[0])])

# Check equality
equal = np.array_equal(r1, r2_correct)
