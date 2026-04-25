
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Reshape to 1D arrays to calculate outer product
r1 = np.outer(X.flatten(), X.flatten())
r2 = np.dot(X.flatten(), X.flatten().T)

print(np.array_equal(r1, r2))  # This will now return True
