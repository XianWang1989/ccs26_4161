
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a 2D array of zeros
    max_index = vector.max() + 1  # account for inclusive maximum
    binary_matrix = np.zeros((vector.size, max_index))

    # Set the corresponding indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
result = transform_to_binary_matrix(v)
print(result)
