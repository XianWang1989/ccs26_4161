
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product
r1 = np.array([np.outer(X[i].A1, X[i].A1) for i in range(X.shape[0])])
# Calculate using dot product (note: using transposition)
r2 = np.dot(X, X.T)

# Compare the results
result = np.array_equal(r1, r2)
print("Arrays are equal:", result)
