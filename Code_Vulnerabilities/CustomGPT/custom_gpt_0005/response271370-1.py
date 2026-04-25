
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Create a binary matrix with additional space for zeros
    C = np.zeros((v.shape[0], v.max() + 1))
    # Set ones at the corresponding indices
    C[np.arange(v.shape[0]), v] = 1
    return C

# Example usage:
v = np.array([1, 5, 3])
result = transform_vector_to_binary_matrix(v)
print(result)
