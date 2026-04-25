
import numpy as np
import scipy.ndimage as ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    kernel = ndimage.gaussian_filter(np.zeros((size, size)), sigma=sigma)
    return kernel

# Parameters
size = 5
sigma = 1.0  # Standard deviation
gaussian_kernel = gaussian_filter(size, sigma)

print(gaussian_kernel)
