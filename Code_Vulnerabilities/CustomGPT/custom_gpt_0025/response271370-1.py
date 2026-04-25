
import numpy as np

def permute_array(vector):
    # Initialize a binary matrix of zeros with shape (number of elements, max value + 1)
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    # Set 1s at positions corresponding to the values in the vector
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3, 0])  # Example vector including zero
binary_matrix = permute_array(v)

print(binary_matrix)
