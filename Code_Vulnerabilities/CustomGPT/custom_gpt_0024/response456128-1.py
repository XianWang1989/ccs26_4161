
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate using np.outer
r1 = np.outer(X.A.flatten(), X.A.flatten())

# Calculate using np.dot (with flattening)
r2 = np.dot(X.A.flatten(), X.A.flatten().T)

# Check equality
result = np.array_equal(r1, r2)
print(result)  # Should print True
