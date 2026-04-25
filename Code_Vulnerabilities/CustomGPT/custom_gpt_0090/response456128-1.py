
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product
r1 = np.outer(X, X)

# To match the outer product, reshape X appropriately
r2 = np.dot(X.T, X)

# Check for equality
result = np.array_equal(r1, r2)

print("r1:", r1)
print("r2:", r2)
print("Are r1 and r2 equal?", result)
