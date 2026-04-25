
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1):
    # Create a 5x5 Gaussian filter
    filter_size = (size, size)
    gaussian_kernel = np.zeros(filter_size)

    for x in range(size):
        for y in range(size):
            gaussian_kernel[x, y] = (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2))

    # Normalize the filter
    gaussian_kernel /= np.sum(gaussian_kernel)

    return gaussian_kernel

# Example usage
gaussian_filter = create_gaussian_filter(5, 1)
print(gaussian_filter)
