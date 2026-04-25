
import numpy as np

def transform_to_binary_matrix(v):
    # Create a zero matrix with shape (number of elements in v, max value in v + 1)
    C = np.zeros((v.size, v.max() + 1))
    # Set ones at the respective index positions from vector v
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])  # Input vector
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
