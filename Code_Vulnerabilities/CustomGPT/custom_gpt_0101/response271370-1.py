
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a 2D array of zeros
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the corresponding indices to 1
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
