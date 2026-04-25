
import numpy as np

def transform_to_binary_matrix(v):
    # Create a zero matrix with shape (number of elements, max value + 1)
    max_value = v.max()
    C = np.zeros((v.size, max_value + 1))
    # Set ones in the corresponding indices
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
