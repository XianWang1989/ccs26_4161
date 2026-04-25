
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a zeros matrix with shape (number of elements, max value + 1)
    max_value = vector.max() + 1  # Include zero
    binary_matrix = np.zeros((vector.size, max_value))

    # Use advanced indexing to set the corresponding indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)
print(C)
