
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer correctly
r1 = np.array([np.outer(X[i], X[i]) for i in range(X.shape[0])])

# Using np.dot with transposed arrays
r2 = np.dot(X.T, X)

# Checking if the results are equal
result = np.array_equal(r1, r2)

print("Outer product result:\n", r1)
print("Dot product result:\n", r2)
print("Do they match?", result)
