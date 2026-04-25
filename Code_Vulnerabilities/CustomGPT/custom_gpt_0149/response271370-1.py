
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix with shape (len(vector), max(vector)+1)
    binary_matrix = np.zeros((len(vector), vector.max() + 1))
    # Set 1s at the appropriate indices based on vector values
    binary_matrix[np.arange(len(vector)), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
