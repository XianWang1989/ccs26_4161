
import numpy as np

def transform_to_binary_matrix(v):
    # Create a zero matrix with shape (number of rows, max index + 1)
    C = np.zeros((v.shape[0], v.max() + 1))
    # Set the positions specified by the vector to 1
    C[np.arange(v.shape[0]), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
