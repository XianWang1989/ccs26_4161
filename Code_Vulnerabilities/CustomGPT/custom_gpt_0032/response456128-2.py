
import numpy as np

# Use 1-D arrays for the outer product
X = np.array([1, 5, 9, 4, 1])

# Calculate the outer product
r1 = np.outer(X, X)  # Shape: (5, 5)

# Reshape or modify to match the expected outer product
r2 = np.outer(X.flatten(), X.flatten())  # 1-D to get the same behavior

# Check if they are equal
result = np.array_equal(r1, r2)  # Should return True
print(result)
