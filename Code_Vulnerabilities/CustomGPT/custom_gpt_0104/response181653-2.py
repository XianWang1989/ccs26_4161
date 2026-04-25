
import numpy as np

def gaussian_kernel(size=5, sigma=1.0):
    # Create a grid of (x,y) coordinates
    x = np.linspace(-size//2 + 1, size//2, size)
    y = np.linspace(-size//2 + 1, size//2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the Gaussian kernel
    gaussian /= np.sum(gaussian)

    return gaussian

# Create the Gaussian filter
kernel = gaussian_kernel(size=5, sigma=1.0)

print(kernel)
