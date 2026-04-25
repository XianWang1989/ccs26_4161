
import numpy as np

def extract_cross_profile(array, center, angle, length):
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate increment for x and y based on the angle
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Center point
    cx, cy = center

    # Prepare arrays to hold the cross profile
    profile = []

    # Extract points in both directions
    for d in range(-length, length + 1):
        # Points in the positive slope direction
        x_pos = int(cx + d * dx)
        y_pos = int(cy + d * dy)

        # Points in the negative slope direction
        x_neg = int(cx + d * dy)
        y_neg = int(cy - d * dx)

        # Check bounds and collect values
        if 0 <= x_pos < array.shape[0] and 0 <= y_pos < array.shape[1]:
            profile.append(array[x_pos, y_pos])

        if 0 <= x_neg < array.shape[0] and 0 <= y_neg < array.shape[1]:
            profile.append(array[x_neg, y_neg])

    return np.array(profile)

# Example usage
array = np.random.rand(100, 100)  # Example 100x100 array
center = (50, 50)
angle = 25
length = 20  # Half-length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
