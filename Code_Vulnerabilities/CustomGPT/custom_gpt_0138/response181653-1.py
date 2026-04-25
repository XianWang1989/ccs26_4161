
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    # Create a 2D grid of (x,y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Compute the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter

    return g

# Create a Gaussian filter
filter_5x5 = gaussian_filter()
print(filter_5x5)
