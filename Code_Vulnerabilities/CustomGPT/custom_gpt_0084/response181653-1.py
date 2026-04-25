
import numpy as np
from scipy.ndimage import gaussian_filter

# Function to create a Gaussian filter
def gaussian_filter_2d(size, sigma):
    # Create a meshgrid
    x, y = np.mgrid[-size:size + 1, -size:size + 1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the filter
    g /= g.sum()
    return g

# Parameters for the Gaussian filter
size = 2  # Will generate a 5x5 filter
sigma = 1.0

# Create the Gaussian filter
gaussian_filter = gaussian_filter_2d(size, sigma)

print(gaussian_filter)
