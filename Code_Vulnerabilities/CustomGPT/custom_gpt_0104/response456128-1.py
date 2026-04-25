
import numpy as np

# Define the matrix X
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Calculate the outer product using np.dot with appropriate reshaping
r2 = np.dot(X.T, X).flatten()

# Check if they are equal
are_equal = np.array_equal(r1, r2)

print("Outer product using np.outer:\n", r1)
print("Outer product calculated using np.dot:\n", r2.reshape(r1.shape))
print("Are they equal? ", are_equal)
