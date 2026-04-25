
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a Gaussian kernel
    kernel = np.zeros((size, size))
    center = size // 2

    for x in range(size):
        for y in range(size):
            kernel[x, y] = (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - center)**2 + (y - center)**2) / (2 * sigma**2))

    return kernel

filter_size = 5  # Size of the filter (5x5)
sigma = 1.0      # Standard deviation

gaussian_kernel = gaussian_filter_2d(filter_size, sigma)
print(gaussian_kernel)
