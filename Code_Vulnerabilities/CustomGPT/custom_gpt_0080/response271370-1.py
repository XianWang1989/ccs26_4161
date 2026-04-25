
import numpy as np

def permute_array(vector):
    # Create a 2D array of zeros with shape (number of rows, max value + 1)
    permut = np.zeros((vector.size, vector.max() + 1))
    # Set the appropriate indices to 1
    permut[np.arange(vector.size), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
C = permute_array(v)
print(C)
