
import numpy as np

def extract_cross_profile(array, center, angle, length):
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate the unit direction vectors
    x_offset = np.cos(theta)
    y_offset = np.sin(theta)

    # Generate the coordinates for the cross profile
    coords = []
    for i in range(-length, length + 1):
        # Diagonal line (positive slope)
        pos_coord = (center[0] + i * x_offset, center[1] + i * y_offset)
        coords.append(pos_coord)

        # Diagonal line (negative slope)
        neg_coord = (center[0] + i * y_offset, center[1] - i * x_offset)
        coords.append(neg_coord)

    # Extract values from the array
    cross_profile = []
    for coord in coords:
        x, y = int(round(coord[0])), int(round(coord[1]))
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            cross_profile.append(array[x, y])

    return cross_profile

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
