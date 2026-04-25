
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1.0):
    # Create a small array of zeros; size will be size x size
    kernel = np.zeros((size, size))

    # Create the filter
    # Use a grid to apply the Gaussian formula
    for x in range(size):
        for y in range(size):
            # Calculate the Gaussian value
            kernel[x, y] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(- ((x - (size-1)/2) ** 2 + (y - (size-1)/2) ** 2) / (2 * sigma ** 2))

    # Normalize the kernel to ensure the sum of the filter is 1
    return kernel / np.sum(kernel)

# Create a 5x5 Gaussian filter with sigma = 1.0
gaussian_filter_5x5 = create_gaussian_filter(5, 1.0)
print(gaussian_filter_5x5)
