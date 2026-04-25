
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 5x5 meshgrid
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian filter
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    g /= g.sum()

    return g

# Create a 5x5 Gaussian filter with sigma = 1
filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)
