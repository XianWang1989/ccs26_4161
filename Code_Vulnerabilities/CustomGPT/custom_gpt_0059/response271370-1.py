
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a zero matrix with shape (number of elements in vector, max value in vector + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Place 1s in the appropriate columns based on the vector values
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)

print(C)
