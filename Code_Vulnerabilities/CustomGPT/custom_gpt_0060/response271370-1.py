
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a 2D array with zeros
    matrix = np.zeros((vector.size, vector.max() + 1))
    # Use advanced indexing to set the appropriate positions to 1
    matrix[np.arange(vector.size), vector] = 1
    return matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
