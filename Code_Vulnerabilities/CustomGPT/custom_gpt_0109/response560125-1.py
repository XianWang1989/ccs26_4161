
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array (for example, a random array)
array = np.random.rand(100, 100)

# Define the center and angle
center = (50, 50)
angle = 25  # degrees

# Convert angle to radians
theta = np.radians(angle)

# Calculate the range for extraction
length = 30  # Length of the cross profile
x_offsets = np.arange(-length, length + 1)
y_offsets = np.arange(-length, length + 1)

# Calculate the rotated coordinates
x_diagonal = center[0] + (x_offsets * np.cos(theta) - y_offsets * np.sin(theta)).astype(int)
y_diagonal = center[1] + (x_offsets * np.sin(theta) + y_offsets * np.cos(theta)).astype(int)

# Ensure coordinates are within array bounds
valid_mask = (x_diagonal >= 0) & (x_diagonal < array.shape[0]) & (y_diagonal >= 0) & (y_diagonal < array.shape[1])
x_diagonal = x_diagonal[valid_mask]
y_diagonal = y_diagonal[valid_mask]

# Extract the diagonal cross profile
cross_profile = array[x_diagonal, y_diagonal]

# Print or plot the results
print("Cross Profile Values:", cross_profile)

# Optional: Visualize the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter(y_diagonal, x_diagonal, color='red', s=2)  # Red points for the cross profile
plt.title('Cross Profile at 25 Degrees')
plt.show()
