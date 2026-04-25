
import numpy as np

def extract_cross_profile(array, center, angle, length):
    center_x, center_y = center
    angle_rad = np.radians(angle)

    # Calculate the offsets based on the angle
    dx = int(length * np.cos(angle_rad) / 2)
    dy = int(length * np.sin(angle_rad) / 2)

    # Generate indices for both diagonals
    neg_diag_indices = [(center_x - i, center_y + i * (dy // dx)) for i in range(-dx, dx + 1)]
    pos_diag_indices = [(center_x + i, center_y + i * (-dy // dx)) for i in range(-dx, dx + 1)]

    # Collect values, ensuring we stay within bounds
    cross_profile = []

    for x, y in neg_diag_indices + pos_diag_indices:
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            cross_profile.append(array[x, y])

    return np.array(cross_profile)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)
angle = 25
length = 20  # Length of cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
