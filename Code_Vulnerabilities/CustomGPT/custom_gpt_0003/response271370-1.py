
import numpy as np

def transform_vector_to_binary_matrix(v):
    # Create a zeros matrix with shape (number of elements in v, max element in v + 1)
    C = np.zeros((v.shape[0], v.max() + 1))

    # Use advanced indexing to set the corresponding indices to 1
    C[np.arange(v.shape[0]), v] = 1 

    return C

# Example usage
v = np.array([1, 5, 3])
binary_matrix = transform_vector_to_binary_matrix(v)
print(binary_matrix)
