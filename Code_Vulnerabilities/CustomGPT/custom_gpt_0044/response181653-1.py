
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-0.5 * (xx**2 + yy**2) / sigma**2)
    return g / g.sum()  # Normalize the filter

# Generate a 5x5 Gaussian filter
filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)
