
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D array
array = np.random.rand(100, 100)

# Parameters
center = (50, 50)
angle = 25  # in degrees
length = 20  # length of the cross profile

# Convert angle to radians
theta = np.radians(angle)

# Calculate direction vectors
dx = np.cos(theta)
dy = np.sin(theta)

# Calculate the points for the cross profile
x1 = int(center[0] + dx * length)
y1 = int(center[1] + dy * length)
x2 = int(center[0] - dx * length)
y2 = int(center[1] - dy * length)

# Extract the cross profile points
x_coords = np.linspace(x2, x1, num=length*2)
y_coords = np.linspace(y2, y1, num=length*2)

# Clip coordinates to valid range
x_coords = np.clip(x_coords, 0, array.shape[0] - 1).astype(int)
y_coords = np.clip(y_coords, 0, array.shape[1] - 1).astype(int)

# Get the cross profile values
cross_profile = array[x_coords, y_coords]

# Plot the array and the cross profile
plt.imshow(array, cmap='gray')
plt.plot(x_coords, y_coords, color='red')
plt.title('Cross Profile at 25 Degrees')
plt.show()

# Display the cross profile values
print("Cross Profile Values:", cross_profile)
