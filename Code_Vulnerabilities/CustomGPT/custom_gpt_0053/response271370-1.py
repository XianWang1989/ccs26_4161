
import numpy as np

def transform_to_binary_matrix(vector):
    # Create the binary matrix with shape (n, max_value + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example Usage
v = np.array([1, 5, 3])  # Vector of integers
C = transform_to_binary_matrix(v)

print(C)
