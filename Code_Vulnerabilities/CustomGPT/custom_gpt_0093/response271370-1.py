
import numpy as np

def transform_to_binary_matrix(v):
    # Create an empty binary matrix with shape (len(v), v.max() + 1)
    C = np.zeros((len(v), v.max() + 1))
    # Set the appropriate indices to 1
    C[np.arange(len(v)), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
