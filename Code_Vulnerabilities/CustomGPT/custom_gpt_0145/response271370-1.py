
import numpy as np

def transform_to_binary_matrix(v):
    # Create a binary matrix of size (len(v), max(v) + 1)
    binary_matrix = np.zeros((len(v), v.max() + 1))

    # Set the ones in the corresponding indices
    binary_matrix[np.arange(len(v)), v] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
