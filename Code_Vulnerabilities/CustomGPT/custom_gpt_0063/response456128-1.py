
import numpy as np

X = np.array([[1, 5],
              [5, 9],
              [4, 1]])

# Compute the outer product using np.outer
r1 = np.outer(X, X)

# Reshape the arrays to use np.dot correctly
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)

print("Result of np.array_equal:", result)
