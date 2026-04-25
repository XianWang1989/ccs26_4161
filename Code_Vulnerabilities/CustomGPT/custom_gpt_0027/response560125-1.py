
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array filled with some values
array = np.random.rand(100, 100)

# Define the center and angle
center = (50, 50)
angle = 25  # in degrees

# Convert angle to radians for calculation
theta = np.radians(angle)

# Create a range for the cross profile
length = 20  # length of the profile
x_offset = np.arange(-length, length + 1)
y_offset = np.arange(-length, length + 1)

# Calculate the rotated coordinates
x_rotated = x_offset * np.cos(theta) - y_offset * np.sin(theta)
y_rotated = x_offset * np.sin(theta) + y_offset * np.cos(theta)

# Center the profile at (50, 50)
cross_profile_x = center[0] + x_rotated
cross_profile_y = center[1] + y_rotated

# Clip coordinates to be within the array boundaries
cross_profile_x = np.clip(cross_profile_x, 0, 99).astype(int)
cross_profile_y = np.clip(cross_profile_y, 0, 99).astype(int)

# Extract the values from the original array
cross_profile_values = array[cross_profile_x, cross_profile_y]

# Print the cross profile values
print(cross_profile_values)

# Optional: Visualize the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter(cross_profile_y, cross_profile_x, color='red')
plt.title(f'Cross Profile at {center} at {angle} degrees')
plt.show()
