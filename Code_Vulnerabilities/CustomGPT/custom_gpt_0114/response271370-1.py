
import numpy as np

def transform_to_binary_matrix(vector):
    # Create a binary matrix with shape (len(vector), max(vector) + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))

    # Set the appropriate indices to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1

    return binary_matrix[:, 1:]  # Exclude the first column for zero indexing

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)
print(binary_matrix)
