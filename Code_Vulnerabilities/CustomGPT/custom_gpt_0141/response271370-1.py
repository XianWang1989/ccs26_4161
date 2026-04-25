
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Determine the maximum value in v to define the matrix size
    max_value = v.max()

    # Create a binary matrix initialized to zeros
    binary_matrix = np.zeros((v.shape[0], max_value + 1))

    # Fill the matrix with ones at the indexed positions
    binary_matrix[np.arange(v.shape[0]), v] = 1

    return binary_matrix

# Example usage:
v = np.array([1, 5, 3])  # Example vector
C = transform_vector_to_binary_matrix(v)

print(C)
