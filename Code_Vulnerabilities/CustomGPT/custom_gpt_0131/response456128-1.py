
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# The outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# To achieve similar structure using np.dot, you need to flatten
# and create an equivalent outer product in terms of dots
# This yields a similar structure but requires reshaping
vec = X.flatten()
r2 = np.dot(vec.reshape(-1, 1), vec.reshape(1, -1))

# Check if they are equal
are_equal = np.array_equal(r1, r2)

print("r1 (using np.outer):")
print(r1)
print("\nr2 (using np.dot):")
print(r2)
print("\nAre they equal?:", are_equal)
