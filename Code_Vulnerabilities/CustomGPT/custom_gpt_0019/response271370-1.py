
import numpy as np

def transform_to_binary_matrix(vector):
    # Initialize a binary matrix with zeros
    rows = vector.shape[0]
    cols = vector.max() + 1  # +1 to account for zero indexing
    binary_matrix = np.zeros((rows, cols), dtype=int)

    # Set the corresponding indices to 1
    binary_matrix[np.arange(rows), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
result = transform_to_binary_matrix(v)
print(result)
