
import numpy as np

def create_binary_matrix(vector):
    # Create a zeroed matrix with shape (number of rows, max value + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = create_binary_matrix(v)
print(binary_matrix)
