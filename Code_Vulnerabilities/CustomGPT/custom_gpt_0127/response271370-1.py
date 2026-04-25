
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix filled with zeros
    num_rows = vector.shape[0]
    num_cols = vector.max() + 1  # Include 0 for proper indexing
    binary_matrix = np.zeros((num_rows, num_cols))

    # Set the appropriate column indices to 1
    binary_matrix[np.arange(num_rows), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
