
import numpy as np

def vector_to_binary_matrix(vec):
    # Create a zero array with rows equal to the length of the vector and columns equal to max(value) + 1
    binary_matrix = np.zeros((len(vec), vec.max() + 1))

    # Use advanced indexing to set the appropriate positions to 1
    binary_matrix[np.arange(len(vec)), vec] = 1

    return binary_matrix

# Example usage:
v = np.array([1, 5, 3])
result = vector_to_binary_matrix(v)
print(result)
