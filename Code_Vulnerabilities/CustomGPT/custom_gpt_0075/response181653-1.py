
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    # Create a 2D grid of (x, y) coordinates
    x, y = np.meshgrid(np.linspace(-size//2, size//2, size), np.linspace(-size//2, size//2, size))

    # Calculate the Gaussian filter values
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter to ensure the sum is 1
    return g / np.sum(g)

# Generate a 5x5 Gaussian filter with sigma=1
gaussian_filter_5x5 = gaussian_filter(size=5, sigma=1)
print(gaussian_filter_5x5)
