
import numpy as np

def gaussian_filter(size, sigma):
    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size//2:size//2 + 1, -size//2:size//2 + 1]

    # Compute the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2.0 * sigma**2))

    # Normalize the filter
    return g / g.sum()

# Define parameters
size = 5  # filter size
sigma = 1.0  # filter standard deviation

# Create the Gaussian filter
gaussian_filter_5x5 = gaussian_filter(size, sigma)
print(gaussian_filter_5x5)
