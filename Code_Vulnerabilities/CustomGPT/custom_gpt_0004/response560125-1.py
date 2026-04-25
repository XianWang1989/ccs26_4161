
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    # Getting the center coordinates
    x0, y0 = center
    angle_rad = np.radians(angle)

    # Calculate the endpoints of the cross profile
    x1 = int(x0 + length * np.cos(angle_rad))
    y1 = int(y0 + length * np.sin(angle_rad))
    x2 = int(x0 - length * np.cos(angle_rad))
    y2 = int(y0 - length * np.sin(angle_rad))

    # Using np.clip to avoid out of bounds errors
    x1, y1 = np.clip((x1, y1), 0, arr.shape[1] - 1)
    x2, y2 = np.clip((x2, y2), 0, arr.shape[1] - 1)

    # Create an empty array to hold the profile
    cross_profile = []

    # Extracting the values along the specified angle
    for step in range(-length, length + 1):
        # Calculate offsets
        dx = int(step * np.cos(angle_rad + np.pi / 2))  # perpendicular direction
        dy = int(step * np.sin(angle_rad + np.pi / 2))

        # Get the points
        x = np.clip(x0 + dx, 0, arr.shape[1] - 1)
        y = np.clip(y0 + dy, 0, arr.shape[0] - 1)

        cross_profile.append(arr[y, x])

    return np.array(cross_profile)

# Example usage
np.random.seed(0)  # For reproducibility
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)
angle = 25  # degrees
length = 20  # Length of the cross profile

profile = extract_cross_profile(array, center, angle, length)

# Visualize the result
plt.plot(profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
