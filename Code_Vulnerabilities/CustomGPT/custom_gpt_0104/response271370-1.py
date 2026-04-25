
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix of zeros with shape (len(vector), max_value + 1)
    max_value = vector.max()
    binary_matrix = np.zeros((vector.shape[0], max_value + 1))

    # Set ones in the positions specified by the vector elements
    # Note: The vector values are taken as indices, thus we need to keep the max value + 1 for zero indexing
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)

print(C)
