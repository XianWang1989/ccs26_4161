
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    kernel = np.zeros((size, size), dtype=np.float32)
    for x in range(size):
        for y in range(size):
            kernel[x, y] = (1/(2 * np.pi * sigma**2)) * np.exp(- ((x - (size // 2))**2 + (y - (size // 2))**2) / (2 * sigma**2))

    return kernel / np.sum(kernel)

filter_5x5 = gaussian_filter(5, 1)
print(filter_5x5)
