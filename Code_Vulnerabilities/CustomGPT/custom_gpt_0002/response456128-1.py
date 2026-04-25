
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X.A.ravel(), X.A.ravel())  # Flatten X for outer product
r2 = np.dot(X.T, X)  # Correct dot product

print(np.array_equal(r1, r2))  # This should return True now
