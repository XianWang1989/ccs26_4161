
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a zeros matrix with shape (number of elements in vector, max value + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))
    # Set the corresponding indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
