
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    """Create a Gaussian filter of given size and sigma."""
    # Create a 2D Gaussian filter
    kernel = np.zeros((size, size), dtype=np.float32)
    mean = size // 2

    for x in range(size):
        for y in range(size):
            kernel[x, y] = (1/(2 * np.pi * sigma ** 2)) * np.exp(-((x - mean) ** 2 + (y - mean) ** 2) / (2 * sigma ** 2))

    # Normalize the kernel
    return kernel / np.sum(kernel)

# Example usage:
size = 5
sigma = 1
gaussian_filter_kernel = create_gaussian_filter(size, sigma)
print(gaussian_filter_kernel)
