
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a meshgrid for filter coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2.0 * sigma**2))

    # Normalize the filter
    g /= g.sum()
    return g

# Create a Gaussian filter of size 5x5 with standard deviation of 1.0
filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)
