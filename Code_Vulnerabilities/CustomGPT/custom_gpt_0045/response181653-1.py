
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 5x5 grid of (x,y) coordinates
    y, x = np.mgrid[-(size // 2):(size // 2) + 1, -(size // 2):(size // 2) + 1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the filter to ensure the sum is 1
    g /= g.sum()
    return g

# Set size and sigma
size = 5  # For 5x5 filter
sigma = 1.0  # Standard deviation

# Generate Gaussian filter
gaussian_filter_array = gaussian_filter(size, sigma)
print(gaussian_filter_array)
