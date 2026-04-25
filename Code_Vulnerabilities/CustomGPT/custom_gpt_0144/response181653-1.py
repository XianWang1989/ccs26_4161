import numpy as np

def gaussian_kernel(size: int, sigma: float):
    """Generate a 2D Gaussian kernel."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return kernel / np.sum(kernel)

# Usage
size = 5
sigma = 1.0
g_kernel = gaussian_kernel(size, sigma)
print(np.round(g_kernel, 7))
