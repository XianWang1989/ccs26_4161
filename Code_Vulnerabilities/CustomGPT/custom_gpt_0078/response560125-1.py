
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D array
array = np.random.rand(100, 100)

# Center point
center = (50, 50)

# Angle in degrees
angle = 25
radians = np.deg2rad(angle)

# Calculate the direction of the diagonal
dx = np.cos(radians)
dy = np.sin(radians)

# Extract the cross profile
length = 50  # Half-length of the cross profile
cross_profile = []

for t in range(-length, length + 1):
    x1 = center[0] + t * dx  # Positive diagonal
    y1 = center[1] + t * dy
    x2 = center[0] + t * dy  # Perpendicular diagonal
    y2 = center[1] - t * dx

    # Append values if they are within bounds
    if 0 <= int(x1) < 100 and 0 <= int(y1) < 100:
        cross_profile.append(array[int(y1), int(x1)])
    if 0 <= int(x2) < 100 and 0 <= int(y2) < 100:
        cross_profile.append(array[int(y2), int(x2)])

# Convert to numpy array for further processing
cross_profile = np.array(cross_profile)

# Example visualization
plt.plot(cross_profile)
plt.title('Cross Profile at 25 degrees')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
