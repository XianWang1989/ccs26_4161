
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a zeros matrix with dimensions (n, max_value + 1)
    n = vector.shape[0]
    max_value = vector.max()
    binary_matrix = np.zeros((n, max_value + 1))

    # Set the corresponding indices to 1
    binary_matrix[np.arange(n), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
