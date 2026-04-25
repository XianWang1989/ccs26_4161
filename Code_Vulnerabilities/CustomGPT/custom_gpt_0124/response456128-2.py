
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product for each row
r1 = np.array([np.outer(X[i], X[i]) for i in range(X.shape[0])])
r1 = np.sum(r1, axis=0)  # Sum to get a final outer-like structure

# Compute dot product
r2 = np.dot(X.T, X)

# Check for equality
result = np.array_equal(r1, r2)
print("Are the results equal?:", result)  # This will be False.
