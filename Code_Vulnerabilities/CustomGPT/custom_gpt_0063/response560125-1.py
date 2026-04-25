
import numpy as np

def extract_cross_profile(array, center, angle_degrees, length):
    # Convert angle to radians
    angle_radians = np.radians(angle_degrees)
    cos_angle = np.cos(angle_radians)
    sin_angle = np.sin(angle_radians)

    # Create an array to hold the cross profile values
    cross_profile = []

    # Loop through length from -length//2 to length//2
    for i in range(-length // 2, length // 2 + 1):
        # Calculate the offsets for diagonal lines
        x_offset = int(i * cos_angle)
        y_offset = int(i * sin_angle)

        # Calculate the coordinates for the cross profile
        x1, y1 = center[0] + x_offset, center[1] + y_offset  # First angle
        x2, y2 = center[0] - x_offset, center[1] - y_offset  # Second angle

        # Add values to the profile if within bounds
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_profile.append(array[y1, x1])  # First diagonal

        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_profile.append(array[y2, x2])  # Second diagonal

    return np.array(cross_profile)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 21  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
