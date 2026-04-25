
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    """
    Create a Gaussian filter.

    Parameters:
    size -- size of the filter (must be an odd number)
    sigma -- standard deviation of the Gaussian

    Returns:
    A 2D Gaussian filter
    """
    if size % 2 == 0:
        raise ValueError("Size must be an odd number.")

    # Generate a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / np.sum(g)  # Normalize the filter

# Example usage
filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)
