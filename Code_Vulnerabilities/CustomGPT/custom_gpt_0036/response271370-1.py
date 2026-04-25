
import numpy as np

def transform_to_binary_matrix(v):
    # Create zero matrix with shape (number of elements in v, max index + 1)
    C = np.zeros((v.shape[0], v.max() + 1))

    # Use advanced indexing to set corresponding indexes to 1
    C[np.arange(v.shape[0]), v] = 1

    return C

# Example usage:
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
