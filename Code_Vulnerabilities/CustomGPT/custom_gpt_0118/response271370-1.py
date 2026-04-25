
import numpy as np

def transform_to_binary_matrix(vector):
    # Add 1 to the vector to handle zero indexing
    vector = vector + 1
    # Create a binary matrix with shape (number of rows, max value + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the corresponding indices to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)

print(C)
