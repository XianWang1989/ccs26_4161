
import numpy as np

def permute_array(vector):
    # Create a binary matrix with zeros
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the specific indices to 1
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
result = permute_array(v)
print(result)
