
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a zero matrix with shape (number of rows, max index + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the appropriate positions to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)
print(C)
