
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix filled with zeros
    rows = vector.shape[0]
    cols = vector.max() + 1  # Adding 1 to accommodate zero indexing
    binary_matrix = np.zeros((rows, cols))

    # Use advanced indexing to set the appropriate positions to 1
    binary_matrix[np.arange(rows), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)
print(C)
