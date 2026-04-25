
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 5x5 grid
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    x, y = np.meshgrid(ax, ax)

    # Define the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter

    return g

# Example usage
filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)
