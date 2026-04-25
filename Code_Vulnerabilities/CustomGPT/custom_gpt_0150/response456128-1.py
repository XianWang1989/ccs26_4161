
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct outer product using np.outer
r1 = np.outer(X, X)

# Adjusted dot product to mimic outer product behavior
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)
print("Are the results equal?", result)
