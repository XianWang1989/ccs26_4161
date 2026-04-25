
import numpy as np

def gaussian_kernel(size: int, sigma: float):
    """Generates a Gaussian kernel."""
    kernel = np.fromfunction(
        lambda x, y: (1/ (2 * np.pi * sigma ** 2)) *
                     np.exp(- ((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2)),
        (size, size)
    )
    return kernel / np.sum(kernel)  # Normalize the kernel

# Parameters
size = 5  # Size of the filter
sigma = 1  # Standard deviation for Gaussian

# Generate Gaussian kernel
gaussian_filter = gaussian_kernel(size, sigma)

print(gaussian_filter)
