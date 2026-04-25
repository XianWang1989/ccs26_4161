
import numpy as np

def extract_cross_profile(arr, center, angle, width=1):
    rows, cols = arr.shape
    y0, x0 = center
    angle_rad = np.radians(angle)

    # Calculate direction vectors based on the angle
    dy = np.sin(angle_rad)
    dx = np.cos(angle_rad)

    # Generate points along the diagonal lines
    points = []
    for w in range(-width, width + 1):
        # Calculate adjusted points for the cross profile
        y1 = int(y0 + w * dy)
        x1 = int(x0 + w * dx)
        y2 = int(y0 - w * dy)
        x2 = int(x0 - w * dx)

        if 0 <= y1 < rows and 0 <= x1 < cols:
            points.append(arr[y1, x1])
        if 0 <= y2 < rows and 0 <= x2 < cols:
            points.append(arr[y2, x2])

    return points

# Example usage
array = np.random.rand(100, 100)  # Example 100x100 2D array
center_point = (50, 50)
angle = 25  # Angle in degrees

cross_profile = extract_cross_profile(array, center_point, angle)
print(cross_profile)
