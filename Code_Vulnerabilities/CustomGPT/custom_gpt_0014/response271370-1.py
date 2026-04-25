
import numpy as np

def transform_to_binary_matrix(vector):
    # Creating a binary matrix with shape (n, max_value + 1)
    matrix = np.zeros((len(vector), vector.max() + 1))
    # Using advanced indexing to set the appropriate positions to 1
    matrix[np.arange(len(vector)), vector] = 1
    return matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
