
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix of shape (len(v), max(v) + 1)
    C = np.zeros((len(v), v.max() + 1))
    # Set the appropriate positions to 1
    C[np.arange(len(v)), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
