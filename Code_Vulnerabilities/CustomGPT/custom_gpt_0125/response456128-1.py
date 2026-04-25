
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct use of np.dot to match np.outer
r1 = np.outer(X, X)  # This will give a different shape when X is a matrix
r2 = np.sum(np.dot(X.T, X), axis=0)  # Adjust this for proper outer product equivalence
np.array_equal(r1, r2)  # Check if they are equal
