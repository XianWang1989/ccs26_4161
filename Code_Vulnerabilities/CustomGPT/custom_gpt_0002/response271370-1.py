
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Create a binary array of shape (len(v), max(v) + 1)
    binary_matrix = np.zeros((v.shape[0], v.max() + 1))

    # Set 1 in the positions corresponding to the values in vector v
    binary_matrix[np.arange(v.shape[0]), v] = 1

    return binary_matrix

v = np.array([1, 5, 3, 0])
result = transform_vector_to_binary_matrix(v)
print(result)
