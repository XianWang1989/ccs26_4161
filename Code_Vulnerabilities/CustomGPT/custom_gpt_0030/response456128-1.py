
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Calculate outer product using np.dot by reshaping
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?:", result)
