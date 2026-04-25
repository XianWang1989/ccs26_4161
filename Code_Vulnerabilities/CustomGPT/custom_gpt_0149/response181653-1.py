
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a 1D Gaussian kernel
    kernel_1d = np.linspace(-(size // 2), size // 2, size)
    kernel_1d = np.exp(-0.5 * (kernel_1d / sigma) ** 2)
    kernel_1d /= kernel_1d.sum()  # Normalize the kernel

    # Create a 2D Gaussian filter by outer product
    kernel_2d = np.outer(kernel_1d, kernel_1d)
    return kernel_2d

# Parameters
size = 5  # filter size (5x5)
sigma = 1.0  # standard deviation

# Generate Gaussian filter
gaussian_filter = gaussian_filter_2d(size, sigma)
print(gaussian_filter)
