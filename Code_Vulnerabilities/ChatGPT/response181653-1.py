
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    kernel_1d = scipy.ndimage.gaussian_filter1d(np.arange(-size//2 + 1, size//2 + 1), sigma)

    # Create a 2D Gaussian kernel by outer product
    kernel_2d = np.outer(kernel_1d, kernel_1d)

    # Normalize the kernel
    kernel_2d /= np.sum(kernel_2d)

    return kernel_2d

# Parameters
filter_size = 5
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_kernel = gaussian_filter(filter_size, sigma)

# Print the filter
print(gaussian_kernel)
