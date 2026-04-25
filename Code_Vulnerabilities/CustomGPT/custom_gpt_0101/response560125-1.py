
import numpy as np

def extract_cross_profile(arr, center, angle, length):
    row, col = center
    angle_rad = np.deg2rad(angle)

    # Calculate direction vector
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    profile = []
    for i in range(-length // 2, length // 2 + 1):
        x = int(col + i * dx)
        y = int(row + i * dy)
        if 0 <= x < arr.shape[1] and 0 <= y < arr.shape[0]:
            profile.append(arr[y, x])

    return np.array(profile)

# Example usage
arr = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)
angle = 25  # degrees
length = 29  # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)
print(cross_profile)
