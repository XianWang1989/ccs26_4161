
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use np.dot with flattened versions of X
r2 = np.dot(X.A1, X.A1.T)

# To check if the results are equal, we can print the result of np.array_equal
print(np.array_equal(np.outer(X.A1, X.A1), r2))  # This should return True
