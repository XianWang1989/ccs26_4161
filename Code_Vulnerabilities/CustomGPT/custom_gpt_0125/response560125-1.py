
import numpy as np

def extract_cross_profile(array, center, angle, length):
    x0, y0 = center
    angle_rad = np.deg2rad(angle)

    # Calculate the deltas for both diagonal directions
    dx = int(length * np.cos(angle_rad))
    dy = int(length * np.sin(angle_rad))

    # Extract the cross profile
    profile = []
    for i in range(-length, length + 1):
        if 0 <= x0 + i < array.shape[0] and 0 <= y0 + i < array.shape[1]:
            profile.append(array[y0 + i][x0 + int(i * (dy/dx))])  # Diagonal +
            profile.append(array[y0 + int(i * (dx/dy))][x0 + i])  # Diagonal -

    return np.array(profile)

# Example usage
arr = np.random.rand(100, 100)  # Create a 100x100 random array
cross_profile = extract_cross_profile(arr, (50, 50), 25, 20)
print(cross_profile)
