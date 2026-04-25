
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a zero matrix with shape (len(vector), max(vector) + 1)
    max_value = vector.max()
    binary_matrix = np.zeros((len(vector), max_value + 1))

    # Set the corresponding indices to 1
    binary_matrix[np.arange(len(vector)), vector] = 1

    return binary_matrix

# Example Usage
v = np.array([1, 5, 3])
result = transform_to_binary_matrix(v)

print(result)
