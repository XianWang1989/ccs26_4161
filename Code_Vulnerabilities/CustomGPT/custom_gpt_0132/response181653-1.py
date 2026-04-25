
import numpy as np

def gaussian_filter(size, sigma):
    """Creates a Gaussian filter of given size and sigma."""
    # Create a 1D Gaussian kernel
    ax = np.linspace(-size // 2 + 1, size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(- (xx**2 + yy**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the kernel
    return g

# Parameters for the Gaussian filter
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

# Print the resulting kernel
print(gaussian_kernel)
