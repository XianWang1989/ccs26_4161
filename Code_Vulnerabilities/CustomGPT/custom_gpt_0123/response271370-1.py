
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a 2D array of zeros with shape (number of rows, max index + 1)
    binary_matrix = np.zeros((len(vector), vector.max() + 1))
    # Set the appropriate indices to 1
    binary_matrix[np.arange(len(vector)), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)

print(C)
