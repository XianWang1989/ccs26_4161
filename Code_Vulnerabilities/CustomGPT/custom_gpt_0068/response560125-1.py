
import numpy as np

def extract_diagonal_cross_profile(array, center, angle, width):
    row, col = center
    angle_rad = np.radians(angle)

    # Compute direction cosines
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Calculate half width of the cross profile
    half_width = width // 2

    # Collect points along the cross profile
    cross_profile = []

    for i in range(-half_width, half_width + 1):
        x1 = int(row + i * dy)  # Vertical displacement
        y1 = int(col + i * dx)  # Horizontal displacement
        x2 = int(row + i * -dy) # Vertical displacement (negative)
        y2 = int(col + i * -dx) # Horizontal displacement (negative)

        # Boundary check to avoid IndexError
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_profile.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_profile.append(array[x2, y2])

    return cross_profile

# Example usage
array = np.random.rand(100, 100)
center = (50, 50)
angle = 25
width = 5
cross_section = extract_diagonal_cross_profile(array, center, angle, width)
print(cross_section)
