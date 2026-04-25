
import numpy as np

def extract_cross_profile(arr, center, angle, length):
    # Get the center point
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate the offsets using the angle
    dx = length * np.cos(angle_rad) // 2
    dy = length * np.sin(angle_rad) // 2

    # Create coordinates for the diagonal profile
    x1 = int(x_center - dx)
    y1 = int(y_center - dy)
    x2 = int(x_center + dx)
    y2 = int(y_center + dy)

    # Extract the cross profile
    cross_profile = []

    for i in range(length):
        # Calculate the coordinates along the angle
        x = int(x1 + (x2 - x1) * i / length)
        y = int(y1 + (y2 - y1) * i / length)

        # Append the value at this coordinate to the cross profile
        cross_profile.append(arr[y % arr.shape[0], x % arr.shape[1]])

    return cross_profile

# Example usage
array_2d = np.random.rand(100, 100)  # Creating a 100x100 random array
center = (50, 50)
angle = 25
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array_2d, center, angle, length)
print(cross_profile)
