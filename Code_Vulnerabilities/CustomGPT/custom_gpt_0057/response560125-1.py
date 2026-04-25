
import numpy as np
import math

def extract_cross_profile(array, center, angle, width=1):
    rows, cols = array.shape
    cx, cy = center
    angle_rad = math.radians(angle)

    # Calculate the direction vectors
    dx = width * np.cos(angle_rad)
    dy = width * np.sin(angle_rad)

    # Generate points for the cross profile
    cross_points = []
    for i in range(-50, 51):  # You can adjust the range based on the desired length of the cross
        x1 = int(cx + i * dy)
        y1 = int(cy + i * dx)
        x2 = int(cx - i * dy)
        y2 = int(cy - i * dx)

        if 0 <= x1 < rows and 0 <= y1 < cols:
            cross_points.append(array[x1, y1])
        if 0 <= x2 < rows and 0 <= y2 < cols:
            cross_points.append(array[x2, y2])

    return np.array(cross_points)

# Example usage
array = np.random.rand(100, 100)
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)
print(cross_profile)
