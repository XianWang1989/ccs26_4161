
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix of shape (number of elements, max value + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))

    # Set the corresponding indices to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
