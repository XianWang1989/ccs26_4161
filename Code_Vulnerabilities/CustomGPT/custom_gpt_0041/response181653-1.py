
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Generates a Gaussian filter.

    Args:
        size (int): The width/height of the filter (must be odd).
        sigma (float): The standard deviation of the Gaussian.

    Returns:
        np.ndarray: The generated Gaussian filter.
    """
    # Ensure size is odd
    if size % 2 == 0:
        size += 1

    # Create a 2D grid of (x,y) coordinates
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)

    # Calculate the Gaussian filter
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    g = g / g.sum()
    return g

# Example usage
filter_size = 5
sigma_value = 1.0
gaussian_filter_result = gaussian_filter(filter_size, sigma_value)
print(gaussian_filter_result)
