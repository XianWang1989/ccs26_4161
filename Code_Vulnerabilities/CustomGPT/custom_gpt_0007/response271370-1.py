
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix with the shape (number of elements in v, maximum value in v + 1)
    C = np.zeros((len(v), v.max() + 1))
    # Use advanced indexing to set the appropriate positions to 1
    C[np.arange(len(v)), v] = 1
    return C

# Example usage:
v = np.array([1, 5, 3, 0])  # Include 0 in the vector
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
