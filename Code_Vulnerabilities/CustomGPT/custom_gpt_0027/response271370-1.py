
import numpy as np

def vector_to_binary_matrix(v):
    # Create a zero matrix with appropriate shape
    C = np.zeros((v.size, v.max() + 1))

    # Set the corresponding indices to 1
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
