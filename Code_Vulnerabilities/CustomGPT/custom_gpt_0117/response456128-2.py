
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute dot product with flattened input
r2 = np.dot(X.flatten(), X.flatten())

# Check equality
result = np.array_equal(r1, r2)
print(f"Are they equal? {result}")  # Should print True
