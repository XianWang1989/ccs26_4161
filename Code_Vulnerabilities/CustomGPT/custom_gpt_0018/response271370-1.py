
import numpy as np

def vector_to_binary_matrix(vector):
    # Calculate the number of rows and the maximum index for columns
    num_rows = vector.shape[0]
    num_cols = vector.max() + 1  # +1 to accommodate zero-based indexing

    # Initialize the binary matrix with zeros
    binary_matrix = np.zeros((num_rows, num_cols))

    # Set ones at specified indices
    binary_matrix[np.arange(num_rows), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)
print(C)
