
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix initialized to zeros
    C = np.zeros((v.size, v.max() + 1))  # Include max+1 to handle zero-based indexing
    # Set the corresponding indices to 1
    C[np.arange(v.size), v] = 1
    return C

# Test with the given vector
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
