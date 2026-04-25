
import numpy as np

def extract_cross_profile(array, center, angle, length):
    # Convert angle from degrees to radians
    angle_rad = np.radians(angle)

    # Calculate directional vectors
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Generate the coordinates for the cross profile
    x_values = []
    y_values = []

    for i in range(-length // 2, length // 2 + 1):
        x1 = int(center[0] + i * dx)
        y1 = int(center[1] + i * dy)
        x2 = int(center[0] - i * dx)
        y2 = int(center[1] - i * dy)

        # Append coordinates if they are within bounds
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            x_values.append(x1)
            y_values.append(y1)
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            x_values.append(x2)
            y_values.append(y2)

    # Extract values from the array using the calculated coordinates
    cross_values = []
    for x, y in zip(x_values, y_values):
        cross_values.append(array[x, y])

    return cross_values

# Example usage
array = np.random.random((100, 100))  # Creating a random 100x100 array
center = (50, 50)
angle = 25  # in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
