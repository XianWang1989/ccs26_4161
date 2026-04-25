
import numpy as np

def transform_to_binary_matrix(v):
    # Create a binary matrix filled with zeros
    C = np.zeros((v.shape[0], v.max() + 1))  # Ensure to have space for the highest index

    # Set the appropriate elements to 1 based on the vector `v`
    C[np.arange(len(v)), v] = 1

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
