
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    kernel_1d = np.linspace(-(size // 2), size // 2, size)
    x = np.exp(-(kernel_1d ** 2) / (2 * sigma ** 2))
    kernel = np.outer(x, x)
    return kernel / np.sum(kernel)  # Normalize the kernel

# Parameters
filter_size = 5
sigma = 1.0

gaussian_filter = create_gaussian_filter(filter_size, sigma)
print(gaussian_filter)
