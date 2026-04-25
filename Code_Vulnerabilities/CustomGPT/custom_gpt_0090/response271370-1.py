
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a zero matrix with shape (number of rows, max value + 1)
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Set ones in the appropriate indices
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)
print(C)
