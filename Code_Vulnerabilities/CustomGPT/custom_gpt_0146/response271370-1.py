
import numpy as np

def transform_to_binary_matrix(v):
    # Create an array of zeros with appropriate shape
    C = np.zeros((v.size, v.max() + 1))  # max + 1 to include the last index

    # Use advanced indexing to assign 1 at the respective indices
    C[np.arange(v.size), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
