
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a binary matrix initialized to zeros
    binary_matrix = np.zeros((vector.size, vector.max() + 1))
    # Set the corresponding indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1
    return binary_matrix

# Example Usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)
print(C)
