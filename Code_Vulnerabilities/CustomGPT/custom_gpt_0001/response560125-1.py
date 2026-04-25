
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.random((100, 100))

# Set the center and angle
center = (50, 50)
angle_degrees = 25
angle_radians = np.radians(angle_degrees)

# Create a range for the length of the cross profile
length = 50  # Length of the cross profile
x_offsets = np.arange(-length, length + 1)
y_offsets_1 = np.tan(angle_radians) * x_offsets
y_offsets_2 = -np.tan(angle_radians) * x_offsets

# Calculate the coordinates for the first and second lines of the cross profile
line1_x = center[0] + x_offsets
line1_y = center[1] + y_offsets_1
line2_x = center[0] + x_offsets
line2_y = center[1] + y_offsets_2

# Ensure coordinates are within the bounds of the array
line1_x = np.clip(line1_x, 0, 99)
line1_y = np.clip(line1_y, 0, 99)
line2_x = np.clip(line2_x, 0, 99)
line2_y = np.clip(line2_y, 0, 99)

# Extract the values along the cross lines
cross_profile = np.zeros((len(x_offsets), 2))
cross_profile[:, 0] = array[line1_y.astype(int), line1_x.astype(int)]
cross_profile[:, 1] = array[line2_y.astype(int), line2_x.astype(int)]

# Visualize the array and cross profile lines
plt.imshow(array, cmap='gray')
plt.plot(line1_x, line1_y, color='red', label='Diagonal 1 (25°)')
plt.plot(line2_x, line2_y, color='blue', label='Diagonal 2 (-25°)')
plt.scatter(*center, color='yellow')  # Mark the center
plt.legend()
plt.title('Cross Profile Extraction')
plt.show()

# Print the extracted cross profile values
print("Cross Profile Values:\n", cross_profile)
