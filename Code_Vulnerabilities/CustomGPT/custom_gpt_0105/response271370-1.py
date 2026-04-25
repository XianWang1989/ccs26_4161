
import numpy as np

def transform_to_binary_matrix(v):
    # Create a binary matrix with zeros
    C = np.zeros((v.size, v.max() + 1))
    # Set 1s in the respective positions indicated by the vector
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
