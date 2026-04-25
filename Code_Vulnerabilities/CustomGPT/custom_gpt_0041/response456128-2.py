
import numpy as np

X = np.array([1, 5, 4])  # 1-D array

# Outer product of X with itself
r1 = np.outer(X, X)

# Dot product of X with its transpose using the proper shape
r2 = np.dot(X[:, np.newaxis], X[np.newaxis, :])  # Make it 2-D

print(np.array_equal(r1, r2))  # This should print True
