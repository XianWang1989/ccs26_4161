
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix of zeros, with shape (number_of_elements, max_value + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Use numpy's advanced indexing to set the appropriate positions to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix


# Example usage:
v = np.array([1, 5, 3, 0])  # Include zero to see its effect
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
