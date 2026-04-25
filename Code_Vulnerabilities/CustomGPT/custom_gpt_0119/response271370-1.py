
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix with shape (n, max_val + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)
print(C)
