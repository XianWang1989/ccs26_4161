
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix with zeros
    rows = vector.size
    cols = vector.max() + 1  # Adjust for 0-based indexing
    binary_matrix = np.zeros((rows, cols))

    # Fill the matrix with ones at the specified indices
    binary_matrix[np.arange(rows), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
