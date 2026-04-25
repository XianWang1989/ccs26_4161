
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Define the center and angle
center = (50, 50)
angle = 25  # degrees

# Generate coordinates for the cross profile
y, x = np.indices(array.shape)
y -= center[0]
x -= center[1]

# Calculate the rotation
theta = np.radians(angle)
x_rotated = x * np.cos(theta) - y * np.sin(theta)
y_rotated = x * np.sin(theta) + y * np.cos(theta)

# Extract values along the rotated lines
cross_profile = []
for dx in range(-50, 51):  # range to cover the cross profile
    cross_profile.append(array[center[0] + dx, center[1]] if 0 <= center[0] + dx < 100 else np.nan)
    cross_profile.append(array[center[0], center[1] + dx] if 0 <= center[1] + dx < 100 else np.nan)

cross_profile = np.array(cross_profile)

# Plotting the array and the extracted cross profile
plt.imshow(array, cmap='gray')
plt.colorbar()
plt.title('Original 2D Array')
plt.show()

plt.plot(cross_profile)
plt.title('Extracted Cross Profile at 25 degrees')
plt.xlabel('Profile Points')
plt.ylabel('Value')
plt.grid()
plt.show()
