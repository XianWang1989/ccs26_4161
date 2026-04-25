
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1.0):
    # Create a 2D Gaussian kernel
    kernel = np.zeros((size, size))
    center = size // 2

    for x in range(size):
        for y in range(size):
            kernel[x, y] = (1/(2 * np.pi * sigma**2)) * \
                           np.exp(-((x - center) ** 2 + (y - center) ** 2) / (2 * sigma**2))

    # Normalize the kernel
    return kernel / kernel.sum()

# Create a 5x5 Gaussian filter
gaussian_filter_5x5 = create_gaussian_filter(size=5, sigma=1.0)
print(gaussian_filter_5x5)
