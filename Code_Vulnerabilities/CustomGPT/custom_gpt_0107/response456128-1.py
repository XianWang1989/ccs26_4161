
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to replicate np.outer using np.dot
r1 = np.outer(X.flatten(), X.flatten())  # Flatten to 1-D for outer
r2 = np.dot(X.T, X)  # Dot product of X.T and X

# Check if they are equal
are_equal = np.array_equal(r1, r2)
print("Are r1 and r2 equal?", are_equal)

print("Result of np.outer:\n", r1)
print("Result of np.dot:\n", r2)
