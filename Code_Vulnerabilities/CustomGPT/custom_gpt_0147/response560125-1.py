
import numpy as np
import math

def extract_cross_profile(array, center, angle_degrees, length):
    # Convert angle to radians
    angle_radians = math.radians(angle_degrees)

    # Center of the cross profile
    x0, y0 = center
    # Calculate offsets
    offset_x = np.arange(-length, length + 1)
    offset_y = np.tan(angle_radians) * offset_x

    # Get the coordinates of the cross profile points
    coordinates = [(int(x0 + dx), int(y0 + dy)) for dx, dy in zip(offset_x, offset_y)]

    # Extract values from the array, handling out-of-bounds 
    profile_values = []
    for x, y in coordinates:
        if 0 <= x < array.shape[1] and 0 <= y < array.shape[0]:
            profile_values.append(array[y, x])

    return profile_values

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50) 
angle = 25 
length = 50  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
