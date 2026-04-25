
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Method 1: Create a Gaussian kernel manually
def create_gaussian_kernel(size, sigma):
    """
    Create a Gaussian kernel.

    Parameters:
    size: Size of the kernel (must be odd, e.g., 5).
    sigma: Standard deviation of the Gaussian distribution.

    Returns:
    A normalized Gaussian kernel.
    """
    # Create a grid of (x, y) coordinates
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian function
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))

    # Normalize the kernel
    kernel /= np.sum(kernel)
    return kernel

# Parameters
size = 5  # Filter size 5x5
sigma = 1.0  # Standard deviation

# Generate the Gaussian kernel
gaussian_kernel = create_gaussian_kernel(size, sigma)
print(gaussian_kernel)

# Method 2: Use scipy's gaussian_filter
# You can visualize the effect of the Gaussian filter on an image
image = np.random.rand(100, 100)  # Example random image
filtered_image = gaussian_filter(image, sigma=sigma)

# Plot the kernel and filtered image
plt.subplot(1, 2, 1)
plt.title('Gaussian Kernel')
plt.imshow(gaussian_kernel, cmap='gray')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Filtered Image')
plt.imshow(filtered_image, cmap='gray')
plt.colorbar()

plt.show()
