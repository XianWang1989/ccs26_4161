
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Vectorized outer product calculation
# Step 1: Convert X to a 2D array (n, 2) and flatten
X_flat = np.asarray(X).reshape(-1)

# Step 2: Compute the outer product using np.outer
r1 = np.outer(X_flat, X_flat)

# Step 3: Compute the product of X and its transpose using np.dot
r2 = np.dot(X, X.T).A  # Convert back to matrix form

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", np.array_equal(r1, r2))
