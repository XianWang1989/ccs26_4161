
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix with an extra column for zero indices
    permut = np.zeros((vector.size, vector.max() + 1))
    permut[np.arange(vector.size), vector] = 1
    return permut

# Example usage
v = np.array([1, 5, 3])
result = transform_to_binary_matrix(v)
print(result)
