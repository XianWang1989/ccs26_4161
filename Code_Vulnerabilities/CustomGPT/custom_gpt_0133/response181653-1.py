
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Generate a Gaussian filter.

    Args:
        size (int): The size of the filter (must be odd).
        sigma (float): The standard deviation of the Gaussian.

    Returns:
        np.ndarray: The Gaussian filter.
    """
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    gaussian_1d = np.exp(-x**2 / (2 * sigma**2))
    gaussian_1d /= gaussian_1d.sum()  # Normalize the kernel

    # Create a 2D Gaussian kernel by outer product
    gaussian_2d = np.outer(gaussian_1d, gaussian_1d)
    return gaussian_2d

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
