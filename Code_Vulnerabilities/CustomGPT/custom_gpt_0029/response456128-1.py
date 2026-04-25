
import numpy as np

# Define a 2D matrix
X = np.array([[1, 5],
              [5, 9],
              [4, 1]])

# Calculate the outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Calculate a matrix dot product
r2 = np.dot(X, X.T).flatten()  # Flatten to 1D

# Check if they are equal
result = np.array_equal(r1, r2)
print("Array equal:", result)
