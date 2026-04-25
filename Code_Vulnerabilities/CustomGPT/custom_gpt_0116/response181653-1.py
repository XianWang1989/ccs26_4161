
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the Gaussian kernel
    return g / g.sum()

# Parameters for the Gaussian filter
size = 2  # Half size of the filter (5x5 will result from size = 2)
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter_2d(size, sigma)
print(gaussian_kernel)
