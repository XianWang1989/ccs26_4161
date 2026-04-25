
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Ensure size is odd
    if size % 2 == 0:
        size += 1

    # Create a 2D grid of (x,y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    return g / np.sum(g)

# Parameters
filter_size = 5
sigma = 1.0

# Generate Gaussian filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)

print(gaussian_filter_5x5)
