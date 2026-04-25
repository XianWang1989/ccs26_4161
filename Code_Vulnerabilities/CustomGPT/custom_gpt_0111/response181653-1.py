
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    # Create a grid of (x,y) coordinates
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / (2 * np.pi * sigma**2)  # Normalize the filter

# Parameters
size = 5
sigma = 1.0

# Generate the filter
gaussian_filter_5x5 = gaussian_filter(size, sigma)
print(gaussian_filter_5x5)
