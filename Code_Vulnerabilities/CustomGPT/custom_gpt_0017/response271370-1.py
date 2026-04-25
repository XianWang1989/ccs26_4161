
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a binary matrix initialized with zeros
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Use np.arange for row indices and set the appropriate columns to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_vector_to_binary_matrix(v)
print(C)
