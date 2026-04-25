
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 2D Gaussian filter
    ax = np.linspace(-size // 2 + 1., size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    g /= np.sum(g)  # Normalize the filter
    return g

# Parameters
filter_size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)
print(gaussian_filter_5x5)
