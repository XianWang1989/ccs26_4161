
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product of the first column of X
first_column = X[:, 0]
r1 = np.outer(first_column, first_column)  # Outer product

# Calculate the dot product of the first column with its transpose
r2 = np.dot(first_column, first_column.T)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", result)
