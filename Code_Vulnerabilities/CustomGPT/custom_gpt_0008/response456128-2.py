
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Create flattened versions of the vectors for outer product calculation
flattened_X1 = X.A.flatten()  # Flattening the matrix to a 1D array
flattened_X2 = X.A.flatten()  # Use the same flattened array for outer product

# Now use np.outer
r1 = np.outer(flattened_X1, flattened_X2)

# For dot product, we need to reshape
r2 = np.dot(X.T.A, X.A)  # Using the transposed flattened for shape alignment

# Check equality
print(np.array_equal(r1, r2))  # Should return True
