
import numpy as np

def extract_diagonal_cross_profile(array, center, angle, length=10):
    # Calculate the angle in radians
    angle_rad = np.radians(angle)

    # Calculate the offsets for the diagonals
    x_offset = length * np.cos(angle_rad)
    y_offset = length * np.sin(angle_rad)

    # Initialize lists to hold the coordinates
    diagonal1 = []
    diagonal2 = []

    # Calculate indices for the cross profile
    for i in range(-length, length + 1):
        # Calculate the indices for the two diagonals
        x1 = int(center[0] + i * y_offset)
        y1 = int(center[1] + i * x_offset)
        x2 = int(center[0] + i * -y_offset)
        y2 = int(center[1] + i * -x_offset)

        # Append to the respective lists if within bounds
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            diagonal1.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            diagonal2.append(array[x2, y2])

    return diagonal1, diagonal2

# Example usage
array = np.random.rand(100, 100)  # Sample 100x100 array
center = (50, 50)
angle = 25
cross_profile = extract_diagonal_cross_profile(array, center, angle)
print(cross_profile)
