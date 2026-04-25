
import numpy as np

# Original matrix
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer (correct usage for vectors)
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot (matrix multiplication with reshaped vectors)
r2 = np.dot(X.T, X)

# For comparison
print("r1 (outer product):")
print(r1)

print("r2 (dot product):")
print(r2)

# Verify if they are equal (they will likely not be)
print("Are r1 and r2 equal?", np.array_equal(r1, r2))

# Adjust r2 to match dimensions of r1 if needed
# This primarily highlights the difference in interpretation
adjusted_r2 = r2.reshape(-1, 1) @ r2.reshape(1, -1)   # mimics outer product structure

print("Adjusted r2 to match outer product structure:")
print(adjusted_r2)

# Check if adjusted r2 matches r1
print("Are adjusted r2 and r1 equal?", np.array_equal(adjusted_r2, r1))
