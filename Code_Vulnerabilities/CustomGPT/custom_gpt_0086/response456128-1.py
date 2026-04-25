
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct usage of np.outer
r1 = np.outer(X, X)

# Reshape to create a version comparable to np.outer
r2 = np.dot(X.T, X)

# Now r2 should match r1 in terms of outer product
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?:", result)
