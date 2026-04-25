
import numpy as np

def transform_vector_to_binary_matrix(vector):
    # Create a zero matrix with shape (number of entries, max value + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))

    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix

# Example usage
v = np.array([1, 5, 3, 0])  # Includes 0 for demonstration
C = transform_vector_to_binary_matrix(v)

print(C)
