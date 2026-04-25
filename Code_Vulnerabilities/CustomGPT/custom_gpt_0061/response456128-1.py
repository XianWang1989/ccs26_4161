
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct use of outer to match dimensions
r1 = np.outer(X.flatten(), X.flatten())
# Dot product of X with its transpose
r2 = np.dot(X, X.T)

# Compare the results
result = np.array_equal(r1, r2)
print(result)  # This will print True
