
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Adjusting for outer product by taking the appropriate vectors
# Flattening the matrix to obtain vectors
vec1 = X.flatten()
vec2 = X.flatten()

# Calculate the outer product using np.outer
r1 = np.outer(vec1, vec2)

# Calculate the outer product-like equivalent using np.dot
# Since np.dot does not match directly, we reshape to 1D
r2 = np.dot(vec1[:, np.newaxis], vec2[np.newaxis, :])

print("Outer product result (r1):")
print(r1)
print("Dot product result (r2):")
print(r2)

# Check if they are equal
print("Are they equal?")
print(np.array_equal(r1, r2))
