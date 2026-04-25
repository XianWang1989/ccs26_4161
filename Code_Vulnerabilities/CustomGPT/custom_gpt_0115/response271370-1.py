
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix of shape (len(vector), max(vector) + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))
    # Place ones at the indices specified by the vector
    binary_matrix[np.arange(vector.shape[0]), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
result = transform_to_binary_matrix(v)

print(result)
