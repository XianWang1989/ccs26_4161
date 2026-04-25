
import numpy as np

def permute_array(vector):
    # Create a binary matrix with extra space for zero-based indexing
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    permut[np.arange(vector.shape[0]), vector] = 1  # Assign 1s based on vector values
    return permut
