
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Determine the shape of the output matrix
    max_index = v.max() + 1  # +1 to accommodate index 0
    C = np.zeros((v.size, max_index), dtype=int)

    # Set the appropriate indices to 1
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
