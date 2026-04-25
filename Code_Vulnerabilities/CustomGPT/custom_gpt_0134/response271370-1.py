
import numpy as np

def vector_to_binary_matrix(vector):
    # Create a binary matrix using np.eye
    return np.eye(vector.size, vector.max() + 1)[np.arange(vector.size), vector]

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)

print(binary_matrix)
