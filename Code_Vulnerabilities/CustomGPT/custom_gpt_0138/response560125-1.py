
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Define the center point and angle
center = (50, 50)
angle = 25  # Degrees

# Convert angle to radians
theta = np.radians(angle)

# Generate the diagonal points
length = 100  # Length of the cross profile
x_offset = np.arange(-length//2, length//2)
y_offset = np.tan(theta) * x_offset

# Get the cross profile coordinates
x_coords = np.clip(center[0] + x_offset, 0, 99)
y_coords = np.clip(center[1] + y_offset, 0, 99)

# Extract the diagonal cross profile
cross_profile = array[y_coords.astype(int), x_coords.astype(int)]

# Plotting the original array and the cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.scatter(center[1], center[0], color='red')  # Center point

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Cross Profile at 25 Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Intensity')
plt.grid()

plt.show()
