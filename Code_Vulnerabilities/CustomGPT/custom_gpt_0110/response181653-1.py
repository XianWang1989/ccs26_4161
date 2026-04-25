
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 2D Gaussian kernel
    kernel = np.fromfunction(
        lambda x, y: (1/ (2 * np.pi * sigma**2)) * 
                     np.exp(-((x - (size-1)/2)**2 + (y - (size-1)/2)**2) / (2 * sigma**2)),
        (size, size)
    )
    return kernel / np.sum(kernel)  # Normalize the kernel

# Example usage
size = 5
sigma = 1.0
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
