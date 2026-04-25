
import numpy as np

def transform_to_binary_matrix(v):
    # Create a zero matrix with shape (number of rows, max value + 1)
    C = np.zeros((v.size, v.max() + 1))

    # Use advanced indexing to set the appropriate elements to 1
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
