
import numpy as np

def vector_to_binary_matrix(vector):
    max_index = vector.max() + 1
    binary_matrix = np.zeros((vector.shape[0], max_index))
    binary_matrix[np.arange(vector.shape[0]), vector] = 1
    return binary_matrix

v = np.array([1, 5, 3])
C = vector_to_binary_matrix(v)

print(C)
