
import numpy as np
import scipy.ndimage as ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()

# Example usage
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation
filter = gaussian_filter(size, sigma)
print(filter)
