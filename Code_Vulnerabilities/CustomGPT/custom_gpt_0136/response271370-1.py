
import numpy as np

def transform_to_binary_matrix(vector):
    # Initialize a matrix of zeros
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    # Set 1s at the specified indices from the vector
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
