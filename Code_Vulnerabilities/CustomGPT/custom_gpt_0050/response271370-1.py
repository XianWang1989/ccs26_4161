
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix with zeros
    C = np.zeros((v.size, v.max() + 1))

    # Use advanced indexing to set the appropriate positions to 1
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
