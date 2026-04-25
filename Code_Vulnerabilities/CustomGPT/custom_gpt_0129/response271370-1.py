
import numpy as np

def vector_to_binary_matrix(vector):
    # Create an array of zeros of shape (number of elements, max value + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Use advanced indexing to place '1's in the correct positions
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
