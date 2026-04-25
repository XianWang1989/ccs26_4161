
import numpy as np
import math
import matplotlib.pyplot as plt

# Create a 100x100 2D array filled with random values
array_2d = np.random.rand(100, 100)

# Center coordinates and angle
center = (50, 50)
angle_degrees = 25
angle_radians = np.radians(angle_degrees)

# Calculate the slope of the diagonal
slope = np.tan(angle_radians)

# Number of points to extract on either side of the center
num_points = 20

# Create lists to hold the indices for the cross profile
cross_profile = []

# Loop through the range of offsets
for offset in range(-num_points, num_points + 1):
    # Calculate indices for the main diagonal and the anti-diagonal
    x_main = center[0] + offset
    y_main = int(center[1] + slope * offset)

    x_anti = center[0] + offset
    y_anti = int(center[1] - slope * offset)

    # Check if the indices are within the bounds of the array
    if 0 <= x_main < array_2d.shape[0] and 0 <= y_main < array_2d.shape[1]:
        cross_profile.append(array_2d[x_main, y_main])

    if 0 <= x_anti < array_2d.shape[0] and 0 <= y_anti < array_2d.shape[1]:
        cross_profile.append(array_2d[x_anti, y_anti])

# Convert the cross profile to a NumPy array and remove duplicates
cross_profile_array = np.unique(cross_profile)

# Output the diagonal cross profile
print("Extracted cross profile centered at (50, 50) at 25 degrees:")
print(cross_profile_array)

# Optionally visualize the original array and cross profile
plt.imshow(array_2d, cmap='gray')
plt.title('Original 2D Array')
plt.scatter([50] * len(cross_profile_array), [50] * len(cross_profile_array), c='red')
plt.show()
