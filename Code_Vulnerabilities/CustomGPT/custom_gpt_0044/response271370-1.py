
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a binary matrix initialized to zeros
    binary_matrix = np.zeros((vector.size, vector.max() + 1))
    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
result = transform_vector_to_binary_matrix(v)
print(result)
