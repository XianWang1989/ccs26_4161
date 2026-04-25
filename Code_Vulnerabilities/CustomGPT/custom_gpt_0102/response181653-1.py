
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]

    # Calculate the 2D Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter to sum to 1
    return g / g.sum()

# Create a 5x5 Gaussian filter with sigma = 1
size = 2  # Half-width
sigma = 1.0
gaussian_kernel = gaussian_filter(size, sigma)

print(gaussian_kernel)
