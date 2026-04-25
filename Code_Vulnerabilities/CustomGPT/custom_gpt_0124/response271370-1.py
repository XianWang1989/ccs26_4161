
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix of shape (number of elements in v, max value in v + 1)
    C = np.zeros((v.size, v.max() + 1))
    # Set the appropriate indices to 1
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
