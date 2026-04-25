
import numpy as np
import scipy.ndimage as ndimage

def gaussian_filter(size, sigma):
    # Create a Gaussian kernel
    kernel = ndimage.gaussian_filter(np.zeros((size, size)), sigma=sigma)
    return kernel

# Parameters
size = 5  # Size of the kernel (5x5)
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

# Print the output
print(gaussian_kernel)
