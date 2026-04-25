
import numpy as np

def transform_to_binary_matrix(v):
    # Create an empty binary matrix with shape (len(v), max(v) + 1)
    C = np.zeros((len(v), v.max() + 1))
    # Set ones in the binary matrix according to the values in v
    C[np.arange(len(v)), v] = 1
    return C

# Sample vector
v = np.array([1, 5, 3])
binary_matrix = transform_to_binary_matrix(v)

print(binary_matrix)
