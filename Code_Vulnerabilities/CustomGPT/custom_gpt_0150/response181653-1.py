
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()

# Generate a Gaussian filter
filter_5x5 = gaussian_filter(size=5, sigma=1)
print(filter_5x5)
