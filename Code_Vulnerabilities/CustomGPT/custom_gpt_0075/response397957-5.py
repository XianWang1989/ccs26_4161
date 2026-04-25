
import numpy as np

def compute_pixels_optimized(myArr, L):
    height, width = myArr.shape
    center_x, center_y = width // 2, height // 2

    # Create coordinate grids
    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)  # Create a meshgrid for pixel coordinates

    # Calculate distances from center
    d = np.sqrt((y - center_y) ** 2 + (x - center_x) ** 2)

    # Apply the function to calculate results
    result = 1 / (1 + d / L)

    return result
