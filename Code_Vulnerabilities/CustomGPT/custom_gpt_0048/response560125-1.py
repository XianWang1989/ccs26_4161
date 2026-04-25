
import numpy as np

def extract_cross_profile(array, center, angle_degrees, length):
    # Convert angle to radians
    angle_radians = np.radians(angle_degrees)

    # Center coordinates
    x_center, y_center = center

    # Calculate the slope based on the angle
    slope = np.tan(angle_radians)

    # Create lists to hold the coordinates of the cross profile
    coords = []

    # Determine end points based on the desired length
    for i in range(-length // 2, length // 2 + 1):
        # Calculate coordinates for the two diagonals
        x1 = int(x_center + i)
        y1 = int(y_center + slope * i)
        x2 = int(x_center + i)
        y2 = int(y_center - slope * i)

        # Append the valid coordinates
        if 0 <= x1 < array.shape[1] and 0 <= y1 < array.shape[0]:
            coords.append(array[y1, x1])
        if 0 <= x2 < array.shape[1] and 0 <= y2 < array.shape[0]:
            coords.append(array[y2, x2])

    return coords

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)
angle = 25
length = 21  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
