
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly use np.outer on 1D arrays
r1 = np.outer(X[0], X[0])  # Outer product of the first row with itself
r2 = np.dot(X[0], X[0].T)   # Matrix multiplication of the first row with itself

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This will return True
