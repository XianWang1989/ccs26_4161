
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer on the flattened version of X
r1 = np.outer(X, X)  # This will give you a larger matrix
r2 = np.einsum('ij,ik->jk', X, X)  # Calculate outer product properly for this case

# Verify the shapes
print(r1.shape)  # Check the output shape of np.outer
print(r2.shape)  # Should match the intended output shape

# Check if they are equal
equal = np.array_equal(r1, r2)
print(equal)  # This should return True if shapes match and values are correct
