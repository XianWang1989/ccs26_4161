
import numpy as np

def vector_to_binary_matrix(v):
    # Determine the number of rows (len(v)) and max index (v.max())
    rows, cols = v.shape[0], v.max() + 1  # Add 1 to accommodate zero index
    # Create a binary matrix of zeros
    C = np.zeros((rows, cols))

    # Set the appropriate positions in the matrix to 1
    C[np.arange(rows), v] = 1

    return C

# Example usage
v = np.array([0, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
