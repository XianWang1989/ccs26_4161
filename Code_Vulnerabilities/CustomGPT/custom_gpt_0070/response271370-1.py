
import numpy as np

def transform_to_binary_matrix(vector):
    # Create an empty binary matrix with the shape (number_of_rows, max_value + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))
    # Set the corresponding indices in the binary matrix to 1
    binary_matrix[np.arange(vector.size), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
