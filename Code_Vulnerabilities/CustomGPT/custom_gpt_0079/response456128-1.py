
import numpy as np

# Define the matrix X
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product
r1 = np.outer(X, X)

# Adjust r2 to use the correct dimensions for the outer product
# Flatten X to ensure it is treated as a vector
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Are r1 and r2 equal?", result)
