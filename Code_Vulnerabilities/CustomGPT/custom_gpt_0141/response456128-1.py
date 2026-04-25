
import numpy as np

# Define the matrix
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Outer product using np.outer
r1 = np.outer(X.A.flatten(), X.A.flatten())  # Flatten the matrix to 1D for the outer product

# Dot product using np.dot (outer product equivalent)
r2 = np.dot(X, X.T)

# Check if they are equal
result_equal = np.array_equal(r1, r2)

print("r1 (outer product):")
print(r1)
print("\nr2 (dot product):")
print(r2)
print("\nAre r1 and r2 equal?", result_equal)
