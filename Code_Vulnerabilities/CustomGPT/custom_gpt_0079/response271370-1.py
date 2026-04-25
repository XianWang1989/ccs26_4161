
import numpy as np

def vector_to_binary_matrix(v):
    # Create a zero matrix with shape (number of elements in v, max value in v + 1)
    C = np.zeros((v.size, v.max() + 1))

    # Set ones at the indices specified by vector v
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
