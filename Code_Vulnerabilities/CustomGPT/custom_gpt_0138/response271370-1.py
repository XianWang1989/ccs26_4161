
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a 2D array of zeros
    binary_matrix = np.zeros((vector.size, vector.max() + 1))
    # Set ones at the specified indices
    binary_matrix[np.arange(vector.size), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
