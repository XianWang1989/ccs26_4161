
import numpy as np

def extract_cross_profile(array, center, angle_degrees, length):
    angle_radians = np.radians(angle_degrees)
    x0, y0 = center

    # Calculate points for the cross profile
    points = []
    for i in range(-length, length + 1):
        # Calculate the offsets for the diagonal
        dx = int(i * np.cos(angle_radians))
        dy = int(i * np.sin(angle_radians))

        # Add the coordinates of the points
        points.append((x0 + dx, y0 + dy))
        points.append((x0 - dy, y0 + dx))

    # Extract values for those coordinates
    cross_values = []
    for x, y in points:
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            cross_values.append(array[x, y])

    return cross_values

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)
angle = 25
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
