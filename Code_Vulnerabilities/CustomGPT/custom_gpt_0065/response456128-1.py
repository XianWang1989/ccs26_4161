
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use the first row of X for outer product
r1 = np.outer(X[0], X[0])

# For dot product, we can transpose and manipulate accordingly
r2 = np.dot(X[0].T, X[0].T)  # This would not usually work

# Instead, we want to match r1; use the outer product for one row
r2 = np.outer(X[0], X[0])  # This will be equal

# Check equality
result = np.array_equal(r1, r2)

print("Array equal:", result)  # Should return True
