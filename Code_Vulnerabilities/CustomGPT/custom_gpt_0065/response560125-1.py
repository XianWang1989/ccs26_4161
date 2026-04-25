
import numpy as np

def extract_cross_profile(arr, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Determine the direction vectors
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Sample points along the cross profile
    profile = []
    for i in range(-length//2, length//2 + 1):
        x = int(x_center + i * dx)
        y = int(y_center + i * dy)

        # Check bounds
        if 0 <= x < arr.shape[0] and 0 <= y < arr.shape[1]:
            profile.append(arr[x, y])

    return profile

# Example usage
arr = np.random.random((100, 100))  # 100x100 array
center = (50, 50)
angle = 25
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)
print(cross_profile)
