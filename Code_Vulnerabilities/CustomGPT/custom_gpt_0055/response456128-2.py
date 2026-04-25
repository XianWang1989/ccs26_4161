
import numpy as np

X = np.array([1, 5, 5, 9, 4, 1]).reshape(2, -1)

r1 = np.outer(X.flatten(), X.flatten())  # Use outer product on flattened array
r2 = np.outer(X, X)  # This is still an outer product

# Now check for equality
print(np.array_equal(r1, r2))  # Should return True
