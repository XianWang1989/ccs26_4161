
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    kernel_1d = np.linspace(-size // 2, size // 2, size)
    kernel_1d = np.exp(-0.5 * (kernel_1d / sigma) ** 2)

    # Normalize the kernel
    kernel_1d /= kernel_1d.sum()

    # Create a 2D Gaussian kernel by outer product
    kernel_2d = np.outer(kernel_1d, kernel_1d)

    return kernel_2d

# Define size and sigma
size = 5
sigma = 1.0  # You can adjust the sigma value as needed

# Generate Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

# Print the output
print(gaussian_kernel)
