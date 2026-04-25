
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Create a binary matrix of zeros with shape (n, max_value + 1)
    C = np.zeros((v.size, v.max() + 1))
    # Set the specified indices to 1
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
