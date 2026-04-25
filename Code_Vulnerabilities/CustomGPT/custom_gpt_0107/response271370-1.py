
import numpy as np

def permute_array(vector):
    # Create a binary matrix with shape (number of rows, max index value + 1)
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the corresponding indices to 1
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
binary_matrix = permute_array(v)

print(binary_matrix)
