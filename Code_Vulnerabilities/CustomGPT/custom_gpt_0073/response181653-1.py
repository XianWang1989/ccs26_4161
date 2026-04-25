
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    # Compute the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the filter
    return g / g.sum()

# Parameters
filter_size = 5
sigma = 1.0

# Create the filter
gaussian_kernel = gaussian_filter(filter_size, sigma)
print(gaussian_kernel)
