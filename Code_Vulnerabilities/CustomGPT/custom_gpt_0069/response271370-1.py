
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix with rows equal to the length of v and columns equal to max value in v plus one
    C = np.zeros((v.shape[0], v.max() + 1))
    # Set the corresponding indices to 1
    C[np.arange(v.shape[0]), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
