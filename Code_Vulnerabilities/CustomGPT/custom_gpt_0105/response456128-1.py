
import numpy as np

# Define the matrix X
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product
r1 = np.outer(X, X)  # Result directly from np.outer

# Reshape and calculate using dot
# Reshape X into vectors
X_reshaped = np.asarray(X).reshape(-1, 1)  # Convert to column vector
r2 = np.dot(X_reshaped, X_reshaped.T)      # Outer product using dot

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This should print True
