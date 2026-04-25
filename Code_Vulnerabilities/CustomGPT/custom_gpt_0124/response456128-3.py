
import numpy as np

# Using a 2D example data
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Adjusted computation
r1 = np.array([np.outer(X[i, :], X[i, :]) for i in range(X.shape[0])])
r2 = np.zeros((X.shape[1], X.shape[1]))

# Aggregate results
for i in range(X.shape[0]):
    r2 += np.outer(X[i, :], X[i, :])

# Check if they are equal
result = np.array_equal(r1, r2)
print("Are the outer products equal?:", result)
