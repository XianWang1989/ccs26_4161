
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    """
    Creates a Gaussian filter.

    :param size: Size of the filter (must be odd).
    :param sigma: Standard deviation of the Gaussian.
    :return: Gaussian filter.
    """
    # Ensure size is odd
    if size % 2 == 0:
        raise ValueError("Size must be odd.")

    # Create an array of the specified size
    gauss = np.zeros((size, size))

    # Calculate the midpoint
    mid = size // 2

    # Create the Gaussian filter
    for x in range(size):
        for y in range(size):
            gauss[x, y] = (1 / (2 * np.pi * sigma ** 2)) * \
                          np.exp(-((x - mid) ** 2 + (y - mid) ** 2) / (2 * sigma ** 2))

    return gauss

# Example usage
size = 5
sigma = 1.0  # Standard deviation
gaussian_filter = create_gaussian_filter(size, sigma)

print(gaussian_filter)
