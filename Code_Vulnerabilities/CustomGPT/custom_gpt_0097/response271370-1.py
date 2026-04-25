
import numpy as np

def permute_array(vector):
    # Create a binary matrix with shape (len(vector), max_value + 1)
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut

# Example vector
v = np.array([1, 5, 3])
binary_matrix = permute_array(v)
print(binary_matrix)
