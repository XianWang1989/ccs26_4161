
import numpy as np

def transform_to_binary_matrix(v):
    # Create an array of zeros with rows equal to the length of v and columns equal to the maximum value in v + 1
    C = np.zeros((v.shape[0], v.max() + 1))

    # Set the appropriate indices to 1
    C[np.arange(v.shape[0]), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
