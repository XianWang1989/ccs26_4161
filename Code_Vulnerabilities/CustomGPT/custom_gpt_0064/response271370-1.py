
import numpy as np

def transform_to_binary_matrix(v):
    # Create a binary matrix of shape (len(v), max(v) + 1)
    C = np.zeros((v.size, v.max() + 1))

    # Set the corresponding indices to 1
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
