
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a binary matrix of shape (len(vector), max(vector) + 1)
    binary_matrix = np.zeros((len(vector), vector.max() + 1))

    # Use advanced indexing to set the appropriate positions to 1
    binary_matrix[np.arange(len(vector)), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)
print(C)
