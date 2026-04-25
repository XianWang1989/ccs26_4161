
import numpy as np

def extract_cross_profile(array, center, angle, length):
    row, col = center
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate offsets
    x_offset = np.arange(-length//2, length//2 + 1) * np.cos(theta)
    y_offset = np.arange(-length//2, length//2 + 1) * np.sin(theta)

    # Create the cross profile
    cross_profile = []
    for x, y in zip(x_offset, y_offset):
        x_idx = int(row + y)
        y_idx = int(col + x)
        if 0 <= x_idx < array.shape[0] and 0 <= y_idx < array.shape[1]:
            cross_profile.append(array[x_idx, y_idx])

    return cross_profile

# Example usage
data = np.random.rand(100, 100)  # 100x100 random array
center = (50, 50)
angle = 25
length = 21  # Length of the cross profile

profile = extract_cross_profile(data, center, angle, length)
print(profile)
