
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use np.outer with 1D arrays
r1 = np.outer(X.flatten(), X.flatten())

# Change r2 to be the outer product using np.outer instead of np.dot
r2 = np.outer(X.flatten(), X.flatten())

# Now we compare the two results
result = np.array_equal(r1, r2)
print(result)  # This should return True
