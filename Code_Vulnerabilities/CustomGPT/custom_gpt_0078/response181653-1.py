
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    gauss = np.exp(-0.5 * (x**2 + y**2) / sigma**2)

    # Normalize the kernel
    return gauss / np.sum(gauss)

# Filter size and standard deviation
size = 5
sigma = 1.0  # Adjust this to control the spread

gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
