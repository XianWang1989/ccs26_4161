
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1):
    # Create a 2D Gaussian kernel
    kernel = np.fromfunction(
        lambda x, y: (
            (1 / (2 * np.pi * sigma**2)) * 
            np.exp(-((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2))
        ), 
        (size, size)
    )
    return kernel

# Example usage
gaussian_filter_5x5 = create_gaussian_filter()
print(gaussian_filter_5x5 / np.sum(gaussian_filter_5x5))  # Normalize the kernel
