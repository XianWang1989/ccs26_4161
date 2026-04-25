
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 5x5 grid
    x, y = np.mgrid[-size:size+1, -size:size+1]
    g = np.exp(-(x**2 + y**2) / (2. * sigma**2))
    return g / g.sum()

# Define size and sigma
size = 2  # Corresponds to a 5x5 filter
sigma = 1.0

# Create the Gaussian filter
gaussian_filter_5x5 = gaussian_filter(size, sigma)
print(gaussian_filter_5x5)
