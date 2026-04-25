
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a Gaussian filter
    filter_size = size // 2 * 2 + 1  # Ensure odd size
    gaussian_filter_2d = np.zeros((filter_size, filter_size))

    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size:size + 1, -size:size + 1]

    # Calculate the Gaussian function
    gaussian_filter_2d = np.exp(-(x**2 + y**2) / (2.0 * sigma**2))

    # Normalize the filter
    gaussian_filter_2d /= gaussian_filter_2d.sum()

    return gaussian_filter_2d

# Parameters
size = 2  # Corresponds to a 5x5 filter (size = 2 means 5 total)
sigma = 1  # Standard deviation

# Create the filter
gaussian_filter_5x5 = create_gaussian_filter(size, sigma)
print(gaussian_filter_5x5)
