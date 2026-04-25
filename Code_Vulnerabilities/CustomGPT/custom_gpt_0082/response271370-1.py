
import numpy as np

def vector_to_binary_matrix(v):
    # Create a binary matrix with shape (len(v), max(v)+1)
    C = np.zeros((len(v), v.max() + 1))

    # Set ones at the positions specified in v
    C[np.arange(len(v)), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
