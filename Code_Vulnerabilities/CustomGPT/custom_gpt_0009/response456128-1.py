
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product using np.outer
r1 = np.outer(X.A.flatten(), X.A.flatten())

# Compute the dot product using np.dot, treating each row as a vector
r2 = np.dot(X.T, X)  # This will produce dot products between rows

# To check if they are equal
print(np.array_equal(r1, r2))  # This will return True
