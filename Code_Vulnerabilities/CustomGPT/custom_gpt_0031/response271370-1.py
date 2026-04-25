
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a binary matrix initialized with zeros
    max_index = np.max(vector)
    binary_matrix = np.zeros((vector.size, max_index + 1))

    # Set ones in the corresponding indices
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)

print(C)
