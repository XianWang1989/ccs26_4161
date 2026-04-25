
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use flattening to get equivalent output
r1 = np.outer(X.flatten(), X.flatten())  # This gives a result corresponding to outer product
r2 = np.dot(X.T, X)  # Transpose to align dimensions

# Check if they are equal
result = np.array_equal(r1, r2)

print("Are r1 and r2 equal?", result)
