
import numpy as np

# Define X as a 2D matrix
X = np.array([1, 5, 4])  # Use 1D arrays for outer product

# Calculate the outer product
r1 = np.outer(X, X)

# Calculate the outer product using np.dot
r2 = np.dot(X[:, np.newaxis], X[np.newaxis, :])

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This should return True

# Print the results
print("Outer product using np.outer:\n", r1)
print("Outer product using np.dot:\n", r2)
