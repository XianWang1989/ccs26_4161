
import numpy as np

def transform_to_binary_matrix(v):
    # Create a binary matrix of zeros
    C = np.zeros((v.size, v.max() + 1))  # Increment max to handle 0 index
    # Set the appropriate indices to 1
    C[np.arange(v.size), v] = 1
    return C

# Example usage
v = np.array([1, 5, 3, 0])  # Include a 0 index
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
