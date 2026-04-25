
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a binary matrix with zeros
    C = np.zeros((vector.shape[0], vector.max() + 1))
    # Set ones at the appropriate indices
    C[np.arange(vector.shape[0]), vector] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
