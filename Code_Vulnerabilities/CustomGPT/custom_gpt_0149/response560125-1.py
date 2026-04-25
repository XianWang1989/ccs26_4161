
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D array
array = np.random.rand(100, 100)

# Parameters
center = (50, 50)  # Center point
angle = 25  # Angle in degrees

# Convert angle to radians
theta = np.radians(angle)

# Calculate the length of the line to extract
length = 50  # Adjust as needed

# Calculate line endpoints
x1 = int(center[0] - length * np.cos(theta))
y1 = int(center[1] - length * np.sin(theta))
x2 = int(center[0] + length * np.cos(theta))
y2 = int(center[1] + length * np.sin(theta))

# Calculate the coordinates of the points on the line
x_coords = np.linspace(x1, x2, num=100).astype(int)
y_coords = np.linspace(y1, y2, num=100).astype(int)

# Ensure coordinates are within bounds
x_coords = np.clip(x_coords, 0, array.shape[0] - 1)
y_coords = np.clip(y_coords, 0, array.shape[1] - 1)

# Extract the diagonal cross profile
cross_profile = array[y_coords, x_coords]

# Output the cross profile
print(cross_profile)

# Optional: Plotting
plt.imshow(array, cmap='gray')
plt.plot(x_coords, y_coords, color='red')
plt.title('Diagonal Cross Profile')
plt.show()
