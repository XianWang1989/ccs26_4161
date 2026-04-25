
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a binary matrix of shape (n, max_value + 1)
    max_value = vector.max()
    binary_matrix = np.zeros((vector.size, max_value + 1))

    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)
print(C)
