
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a binary matrix of shape (len(vector), max(vector)+1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))

    # Set ones in the positions defined by the vector
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
