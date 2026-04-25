
import numpy as np

def transform_to_binary_matrix(vector):
    # Create an array filled with zeros
    max_value = vector.max() + 1  # Ensure we accommodate the max index
    binary_matrix = np.zeros((vector.shape[0], max_value))

    # Set the appropriate indices to 1
    rows = np.arange(vector.shape[0])
    binary_matrix[rows, vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
