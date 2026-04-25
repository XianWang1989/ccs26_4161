
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create an empty filter
    filter_shape = (size, size)
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    # Calculate the Gaussian filter
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the filter
    return g / g.sum()

# Example parameters
size = 5  # filter size
sigma = 1  # standard deviation

gaussian_filter = create_gaussian_filter(size, sigma)
print(gaussian_filter)
