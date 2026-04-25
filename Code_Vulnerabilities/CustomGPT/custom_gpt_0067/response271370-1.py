
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a zero matrix with shape (len(vector), max(vector) + 1)
    binary_matrix = np.zeros((len(vector), vector.max() + 1))

    # Set ones at the appropriate indices
    binary_matrix[np.arange(len(vector)), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
