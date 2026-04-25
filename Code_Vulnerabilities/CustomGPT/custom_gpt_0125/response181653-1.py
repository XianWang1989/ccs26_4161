
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1.0):
    # Create a 5x5 Gaussian filter
    kernel = np.zeros((size, size))
    # Calculate the center of the kernel
    center = size // 2
    for x in range(-center, center + 1):
        for y in range(-center, center + 1):
            kernel[x + center, y + center] = (1/(2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)  # Normalize the kernel

# Create the Gaussian filter
gaussian_filter = create_gaussian_filter()
print(gaussian_filter)
