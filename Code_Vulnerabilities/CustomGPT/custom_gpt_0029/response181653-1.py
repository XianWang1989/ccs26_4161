
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    kernel_1d = np.exp(-0.5 * (np.arange(-size//2 + 1, size//2 + 1) ** 2) / sigma ** 2)
    kernel_1d /= np.sum(kernel_1d)  # Normalize the kernel

    # Create a 2D Gaussian kernel by outer product
    kernel_2d = np.outer(kernel_1d, kernel_1d)
    return kernel_2d

# Parameters for the Gaussian filter
filter_size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(filter_size, sigma)
print(gaussian_kernel)
