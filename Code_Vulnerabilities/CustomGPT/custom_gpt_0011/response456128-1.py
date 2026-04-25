
import numpy as np

# Define the matrix X
X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product
r1 = np.outer(X.flatten(), X.flatten())

# Compute using np.dot
# Here we can stack the flattened arrays vertically
r2 = np.dot(X.T, X)

# Check if arrays are equal
result = np.array_equal(r1, r2)

print(f"r1 (outer product): \n{r1}")
print(f"r2 (dot product): \n{r2}")
print(f"Are r1 and r2 equal? {result}")
