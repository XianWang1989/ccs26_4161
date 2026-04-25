
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a zero matrix with shape (len(vector), max(vector) + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))

    # Use np.arange to place 1s in the correct positions
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
C = transform_to_binary_matrix(v)
print(C)
