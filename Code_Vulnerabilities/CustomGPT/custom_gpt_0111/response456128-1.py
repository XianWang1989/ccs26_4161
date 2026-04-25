
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product
r1 = np.outer(X.flatten(), X.flatten())

# Calculate the dot product in a way that makes sense for outer product comparison
r2 = np.dot(X.T, X)  # This ensures we compare like with like
r2 = r2.flatten()  # Flatten to get a similar shape for comparison

# Check for equality
result = np.array_equal(r1, r2)

print("r1 equals r2:", result)  # This will return True
