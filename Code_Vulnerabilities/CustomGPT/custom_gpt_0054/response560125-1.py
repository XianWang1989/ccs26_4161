
import numpy as np

def extract_cross_profile(array, center, angle_degrees, length):
    angle_radians = np.radians(angle_degrees)
    cos_angle = np.cos(angle_radians)
    sin_angle = np.sin(angle_radians)

    # Calculate the coordinates for the diagonal cross
    cross_coords = []
    for i in range(-length, length + 1):
        x = center[0] + i * cos_angle
        y = center[1] + i * sin_angle
        if 0 <= int(x) < array.shape[0] and 0 <= int(y) < array.shape[1]:
            cross_coords.append(array[int(x), int(y)])

    return np.array(cross_coords)

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 50  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
