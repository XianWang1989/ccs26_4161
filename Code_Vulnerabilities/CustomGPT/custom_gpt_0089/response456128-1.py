
import numpy as np

# Define X as a 1-D array to match the outer product definition
X = np.array([1, 5, 9])  # Use a 1-D array for outer product

# Calculate outer product
r1 = np.outer(X, X)

# Compute dot product using correct reshaping
r2 = np.dot(X[:, np.newaxis], X[np.newaxis, :])  # Broadcast to create a 2-D outer product

# Check for equality
result = np.array_equal(r1, r2)
print("Are the results equal?", result)
