
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D array
array = np.random.rand(100, 100)

# Function to extract the cross profile
def extract_cross_profile(array, center, angle, length=20):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate the offsets for the cross
    offsets = np.arange(-length, length + 1)

    # Calculate coordinates for the horizontal and vertical lines
    horizontal_x = x_center + offsets
    horizontal_y = y_center + np.tan(angle_rad) * offsets

    vertical_x = x_center + np.tan(angle_rad) * offsets
    vertical_y = y_center + offsets

    # Filter to stay within the bounds of the array
    horizontal_coords = [(int(x), int(y)) for x, y in zip(horizontal_x, horizontal_y) if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]]
    vertical_coords = [(int(x), int(y)) for x, y in zip(vertical_x, vertical_y) if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]]

    cross_profile = []

    for x, y in horizontal_coords + vertical_coords:
        cross_profile.append(array[x, y])

    return cross_profile

# Example usage
cross_profile = extract_cross_profile(array, center=(50, 50), angle=25)

# Print cross profile values
print(cross_profile)

# For visualization
plt.imshow(array, cmap='gray')
plt.scatter(*zip(*[(50 + np.arange(-20, 21), 50 + np.tan(np.deg2rad(25)) * np.arange(-20, 21))]), color='red', s=10)  # Horizontal
plt.scatter(*zip(*[(50 + np.tan(np.deg2rad(25)) * np.arange(-20, 21), 50 + np.arange(-20, 21))]), color='blue', s=10)  # Vertical
plt.scatter(50, 50, color='green', s=100)  # Center point
plt.show()
