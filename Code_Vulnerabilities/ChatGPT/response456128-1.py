
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product directly using np.outer
r1 = np.outer(X[:, 0], X[:, 1])  # Taking the first column and second column

# Calculate using np.dot with the transpose of each column
r2 = np.dot(X[:, 0], X[:, 1].T)  # Taking the first column and second column

# Compare the results
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", result)
