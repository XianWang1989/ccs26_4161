
import numpy as np

def permute_array(vector):
    permut = np.zeros((vector.shape[0], vector.max() + 1))
    permut[np.arange(vector.shape[0]), vector] = 1
    return permut
