
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # Produces a higher dimension array
r2 = np.dot(X, X.T)  # Produces a 2D matrix
np.array_equal(r1, r2)  # This will be False
