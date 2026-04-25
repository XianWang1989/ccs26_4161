
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a zero matrix with shape (number of rows, max value + 1)
    max_value = vector.max()
    binary_matrix = np.zeros((vector.shape[0], max_value + 1))

    # Set the appropriate indices in the matrix to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
