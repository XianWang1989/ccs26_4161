
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct way to get outer product using np.dot
r1 = np.outer(X.flatten(), X.flatten())
r2 = np.dot(X.T, X)

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # Should return True
