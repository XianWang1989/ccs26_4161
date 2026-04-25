
import numpy as np
import scipy.ndimage as ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    # Create a 1D Gaussian kernel
    kernel1d = np.linspace(-(size // 2), size // 2, size)
    kernel1d = np.exp(-0.5 * (kernel1d / sigma) ** 2)
    kernel1d /= np.sum(kernel1d)  # Normalize

    # Create a 2D Gaussian filter
    kernel2d = np.outer(kernel1d, kernel1d)
    return kernel2d

# Parameters
filter_size = 5  # 5x5 filter
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)
print(gaussian_filter_5x5)
