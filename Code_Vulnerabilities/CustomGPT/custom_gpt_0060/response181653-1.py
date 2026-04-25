
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter.

    Args:
        size (int): The size of the filter.
        sigma (float): The standard deviation for the Gaussian kernel.

    Returns:
        np.ndarray: A 2D numpy array representing the Gaussian filter.
    """
    # Create a 1D Gaussian kernel
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian function
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / np.sum(g)  # Normalize the kernel

# Example to create a 5x5 Gaussian filter with sigma = 1
filter_size = 5
sigma_value = 1

gaussian_kernel = gaussian_filter(filter_size, sigma_value)
print(gaussian_kernel)
