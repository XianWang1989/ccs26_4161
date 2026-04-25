
import numpy as np

# Define a 1D array for the outer product
x = np.array([1, 5])
y = np.array([5, 9])

# Using np.outer to calculate the outer product
r1 = np.outer(x, y)

# Using np.dot to calculate the outer product representation
# Note that np.dot expects flat arrays for proper outer-like behavior
r2 = np.dot(x[:, np.newaxis], y[np.newaxis, :])

# Verify if they are equal
result = np.array_equal(r1, r2)

print("Outer Product using np.outer:\n", r1)
print("Equivalent Representation using np.dot:\n", r2)
print("Are they equal?:", result)
