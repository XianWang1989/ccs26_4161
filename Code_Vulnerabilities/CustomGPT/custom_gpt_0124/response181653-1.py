
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian filter
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    g /= np.sum(g)  # Normalize the filter

    return g

# Generate a 5x5 Gaussian filter with sigma=1.0
filter = gaussian_filter(size=5, sigma=1.0)
print(filter)
