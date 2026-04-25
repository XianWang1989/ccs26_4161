
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_kernel(size=(5, 5), sigma=1):
    """Generates a Gaussian kernel.

    Args:
        size (tuple): Size of the kernel (height, width).
        sigma (float): Standard deviation of the Gaussian filter.

    Returns:
        np.ndarray: The generated Gaussian filter.
    """
    # Create a 2D grid of (x, y) coordinates
    x = np.linspace(-size[0] // 2 + 1, size[0] // 2, size[0])
    y = np.linspace(-size[1] // 2 + 1, size[1] // 2, size[1])
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)  # Normalize to make the sum of the kernel equal to 1

    return kernel

# Example usage
size = (5, 5)
sigma = 1.0
gaussian_filter = gaussian_kernel(size=size, sigma=sigma)
print(gaussian_filter)
