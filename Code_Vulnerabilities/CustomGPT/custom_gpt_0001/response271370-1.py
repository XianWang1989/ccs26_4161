
import numpy as np

def permute_array(vector):
    # Create a 2D array filled with zeros
    permut = np.zeros((vector.size, vector.max() + 1))
    # Use advanced indexing to set the appropriate indices to 1
    permut[np.arange(vector.size), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
binary_matrix = permute_array(v)

print(binary_matrix)
