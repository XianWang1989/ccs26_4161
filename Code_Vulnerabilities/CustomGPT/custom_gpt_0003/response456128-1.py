
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# outer product
r1 = np.outer(X.A.flatten(), X.A.flatten())

# Dot product and reshape
r2 = np.dot(X, X.T).A.flatten()

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal? :", result)
