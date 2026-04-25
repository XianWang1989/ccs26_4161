
import numpy as np

def transform_to_binary_matrix(vector):
    # Create an array of zeros with shape (number of elements, max value + 1)
    binary_matrix = np.zeros((vector.shape[0], vector.max() + 1))
    # Set the positions specified by the vector to 1
    binary_matrix[np.arange(vector.shape[0]), vector] = 1
    return binary_matrix

# Example usage
v = np.array([1, 5, 3])
result = transform_to_binary_matrix(v)

print(result)
