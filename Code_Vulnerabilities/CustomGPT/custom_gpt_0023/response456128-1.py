
import numpy as np

# Define the input as a 1D array (flatten the matrix)
X = np.array([1, 5, 5, 9, 4, 1]).reshape(3, 2)  # Reshape as needed

# Calculate the outer product
r1 = np.outer(X.flatten(), X.flatten())

# Calculate the dot product
r2 = np.dot(X, X.T)

# Check if the results are equal
equal = np.array_equal(r1, r2)

print("Outer product (r1):")
print(r1)
print("\nDot product (r2):")
print(r2)
print("\nAre they equal?", equal)
