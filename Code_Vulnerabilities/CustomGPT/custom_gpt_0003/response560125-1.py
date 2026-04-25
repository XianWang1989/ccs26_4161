
import numpy as np

def extract_cross_profile(array, center, angle_degrees, length):
    angle_radians = np.radians(angle_degrees)
    cx, cy = center

    # Calculate the direction vectors for the cross shape
    dx = np.cos(angle_radians)
    dy = np.sin(angle_radians)

    # Generate points along the cross profile
    points = []

    # Vertical line points
    for i in range(-length//2, length//2 + 1):
        x1 = cx + i * dy
        y1 = cy - i * dx
        if 0 <= int(x1) < array.shape[0] and 0 <= int(y1) < array.shape[1]:
            points.append(array[int(x1), int(y1)])

    # Horizontal line points
    for i in range(-length//2, length//2 + 1):
        x2 = cx + i * dx
        y2 = cy + i * dy
        if 0 <= int(x2) < array.shape[0] and 0 <= int(y2) < array.shape[1]:
            points.append(array[int(x2), int(y2)])

    return points

# Example usage
array = np.random.rand(100, 100)  # Creating a 100x100 random array
center = (50, 50)
angle = 25  # angle in degrees
length = 10  # length of the cross

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
