
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a 2D Gaussian filter using meshgrid
    x, y = np.mgrid[-size:size+1, -size:size+1]
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter
    return g

# Parameters
size = 2  # (size = 2 creates a 5x5 filter)
sigma = 1.0  # Standard deviation

gaussian_filter_5x5 = create_gaussian_filter(size, sigma)
print(gaussian_filter_5x5)
