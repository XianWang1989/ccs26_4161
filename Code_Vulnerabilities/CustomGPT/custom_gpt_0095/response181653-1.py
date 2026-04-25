
import numpy as np

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian function
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))

    # Normalize the kernel
    return g / np.sum(g)

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
