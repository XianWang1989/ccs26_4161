
import numpy as np

def compute_pixels_brute(myArr, L):
    height, width = myArr.shape
    center_x, center_y = width // 2, height // 2
    result = np.zeros_like(myArr, dtype=float)

    for i in range(height):
        for j in range(width):
            d = np.sqrt((i - center_y) ** 2 + (j - center_x) ** 2)
            result[i, j] = 1 / (1 + d / L)

    return result
