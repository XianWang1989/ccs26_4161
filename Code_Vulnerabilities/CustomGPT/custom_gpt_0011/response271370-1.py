
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Create a binary matrix of zeros
    C = np.zeros((v.shape[0], v.max() + 1))
    # Set the appropriate indices to 1
    C[np.arange(v.shape[0]), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3, 0])  # Input vector
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
