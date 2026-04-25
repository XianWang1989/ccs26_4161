
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D array
array = np.random.rand(100, 100)

# Center point and angle
center = (50, 50)
angle = 25  # in degrees

# Convert the angle to radians
theta = np.radians(angle)

# Calculate the shift in x and y
dx = np.cos(theta)
dy = np.sin(theta)

# Create lists to hold the cross profile points
x_points = []
y_points = []

# Extract points along the cross profile
for t in range(-50, 51):
    x1 = int(center[0] + t * dx)
    y1 = int(center[1] + t * dy)
    x2 = int(center[0] - t * dx)
    y2 = int(center[1] - t * dy)

    if 0 <= x1 < 100 and 0 <= y1 < 100:
        x_points.append(x1)
        y_points.append(y1)
    if 0 <= x2 < 100 and 0 <= y2 < 100:
        x_points.append(x2)
        y_points.append(y2)

# Extract the values from the original array
cross_profile = [array[y, x] for x, y in zip(x_points, y_points)]

# Display the cross profile
plt.plot(cross_profile)
plt.title(f'Cross Profile at {angle} Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
