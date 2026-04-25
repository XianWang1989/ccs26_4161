
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly use np.outer with flattened arrays
r1 = np.outer(X.flatten(), X.flatten())

# Using np.dot on the flattened version too
r2 = np.dot(X.flatten(), X.flatten())

# Check if they are equal
are_equal = np.array_equal(r1, r2)

print("Are r1 and r2 equal?", are_equal)
