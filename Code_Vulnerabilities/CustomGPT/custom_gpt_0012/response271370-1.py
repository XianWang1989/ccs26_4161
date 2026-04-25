
import numpy as np

def vector_to_binary_matrix(vector):
    # Ensure the vector is a numpy array
    vector = np.array(vector)

    # Create the binary matrix using the shape based on the vector
    binary_matrix = np.zeros((vector.size, vector.max() + 1))

    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.size), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
binary_matrix = vector_to_binary_matrix(v)
print(binary_matrix)
