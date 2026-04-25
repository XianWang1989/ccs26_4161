
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=50):
    angle_rad = np.radians(angle)
    x_center, y_center = center

    # Calculate direction vectors
    dx = np.round(length * np.cos(angle_rad)).astype(int)
    dy = np.round(length * np.sin(angle_rad)).astype(int)

    # Collect values along both diagonals
    cross_profile = []

    for t in range(-length, length + 1):
        x1 = x_center + t
        y1 = y_center + (t * dy) // dx if dx != 0 else y_center  # line y = mx + b

        x2 = x_center + (t * dx) // dy if dy != 0 else x_center  # perpendicular line
        y2 = y_center + t

        if 0 <= x1 < array.shape[1] and 0 <= y1 < array.shape[0]:
            cross_profile.append(array[y1, x1])
        if 0 <= x2 < array.shape[1] and 0 <= y2 < array.shape[0]:
            cross_profile.append(array[y2, x2])

    return np.array(cross_profile)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

print("Cross profile values:", cross_profile)
