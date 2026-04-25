
import numpy as np

def gaussian_kernel(size, sigma):
    """Generate a Gaussian kernel."""
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

# Parameters
size = 5
sigma = 1.0
gaussian_kernel = gaussian_kernel(size, sigma)

print(gaussian_kernel)
