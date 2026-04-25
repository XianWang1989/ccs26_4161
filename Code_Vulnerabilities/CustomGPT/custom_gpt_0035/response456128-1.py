
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct calculation
r1 = np.outer(X.flatten(), X.flatten())
r2 = np.dot(X.flatten(), X.flatten().T)

# Verify equality
result = np.array_equal(r1, r2)
print("Are they equal?", result)  # This should be True
