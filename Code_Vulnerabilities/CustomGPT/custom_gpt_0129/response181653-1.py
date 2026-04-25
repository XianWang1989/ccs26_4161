
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size: int, sigma: float) -> np.ndarray:
    """
    Create a 2D Gaussian filter.

    Parameters:
    - size: The size of the filter (should be an odd integer).
    - sigma: The standard deviation of the Gaussian distribution.

    Returns:
    - A normalized 2D Gaussian filter.
    """
    # Create a 2D grid of (x,y) coordinates
    ax = np.arange(-size//2 + 1., size//2 + 1.)
    x, y = np.meshgrid(ax, ax)

    # Compute the 2D Gaussian function
    g = np.exp(- (x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter to ensure that the sum is 1
    return g / np.sum(g)

# Example usage
filter_size = 5  # 5x5 filter
sigma = 1.0      # Standard deviation
gaussian_filter = gaussian_filter_2d(filter_size, sigma)
print(gaussian_filter)
