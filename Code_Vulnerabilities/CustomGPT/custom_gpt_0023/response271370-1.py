
import numpy as np

def transform_to_binary_matrix(v):
    # Create a zero matrix with dimensions (number of rows, max value + 1)
    C = np.zeros((v.shape[0], v.max() + 1))
    # Set the appropriate indices to 1
    C[np.arange(v.shape[0]), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
