
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 2D Gaussian kernel
    g = np.zeros((size, size), dtype=np.float32)
    offset = size // 2
    for x in range(-offset, offset + 1):
        for y in range(-offset, offset + 1):
            g[x + offset, y + offset] = (1 / (2 * np.pi * sigma**2)) * \
                                         np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g

# Generate a 5x5 Gaussian filter with sigma
filter_size = 5
sigma = 1.0
gaussian_filter_matrix = gaussian_filter(size=filter_size, sigma=sigma)

print(gaussian_filter_matrix)
