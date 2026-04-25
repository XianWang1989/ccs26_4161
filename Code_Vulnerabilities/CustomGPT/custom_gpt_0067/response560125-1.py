
import numpy as np

# Create a 100x100 sample array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate offsets
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Create lists to store cross profile points
    points = []

    # Extract points in both diagonal directions
    for i in range(-length, length + 1):
        # Diagonal: /
        x1 = int(x_center + i * dx)
        y1 = int(y_center + i * dy)
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            points.append(array[x1, y1])

        # Diagonal: \
        x2 = int(x_center + i * dy)
        y2 = int(y_center - i * dx)
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            points.append(array[x2, y2])

    return points

# Define parameters
center = (50, 50)
angle = 25
length = 50  # Length of the cross profile

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

print(cross_profile)
