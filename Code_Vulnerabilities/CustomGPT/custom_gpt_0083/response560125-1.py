
import numpy as np

def extract_cross_profile(array, center, angle, length=50):
    center_y, center_x = center
    angle_rad = np.radians(angle)

    # Calculate offsets
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Create indices for the cross profile
    cross_indices = []
    for i in range(-length, length + 1):
        # Calculate positions for the diagonal
        x1 = int(center_x + i * dx)
        y1 = int(center_y + i * dy)
        x2 = int(center_x + i * -dx)
        y2 = int(center_y + i * -dy)

        # Append valid indices
        if 0 <= x1 < array.shape[1] and 0 <= y1 < array.shape[0]:
            cross_indices.append(array[y1, x1])
        if 0 <= x2 < array.shape[1] and 0 <= y2 < array.shape[0]:
            cross_indices.append(array[y2, x2])

    return np.array(cross_indices)

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees

cross_profile = extract_cross_profile(array, center, angle)
print(cross_profile)
