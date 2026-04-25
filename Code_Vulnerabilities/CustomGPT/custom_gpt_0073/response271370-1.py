
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a zero-filled matrix with shape (length of vector, max value + 1)
    binary_matrix = np.zeros((len(vector), vector.max() + 1))

    # Set the corresponding positions to 1
    binary_matrix[np.arange(len(vector)), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_vector_to_binary_matrix(v)
print(C)
