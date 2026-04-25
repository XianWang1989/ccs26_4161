
import numpy as np
from scipy import ndimage

def gaussian_filter(size=5, sigma=1.0):
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / np.sum(g)

filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)
