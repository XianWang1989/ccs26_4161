
import numpy as np

def create_binary_matrix(v):
    # Create a zero matrix of shape (number of elements in v, max value in v + 1)
    C = np.zeros((v.size, v.max() + 1))
    # Use fancy indexing to assign 1s at the appropriate indices
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = create_binary_matrix(v)
print(binary_matrix)
