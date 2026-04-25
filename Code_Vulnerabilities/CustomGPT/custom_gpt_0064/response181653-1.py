
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a 2D Gaussian filter
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    g = g / g.sum()  # Normalize the filter
    return g

# Parameters
size = 5  # Filter size
sigma = 1.0  # Standard deviation

# Generate filter
gaussian_filter_output = gaussian_filter_2d(size, sigma)
print(gaussian_filter_output)
