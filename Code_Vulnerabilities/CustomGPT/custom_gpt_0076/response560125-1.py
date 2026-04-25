
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 2D array
array = np.random.rand(100, 100)

# Center coordinates and angle
center = (50, 50)
angle = 25

# Convert angle from degrees to radians
theta = np.radians(angle)

# Calculate the direction vectors for the cross profile
dx = np.cos(theta)
dy = np.sin(theta)

# Extracting the cross profile
cross_profile = []
for t in range(-50, 51):
    x1 = int(center[0] + t * dx)
    y1 = int(center[1] + t * dy)
    x2 = int(center[0] + t * dy)   # Perpendicular direction
    y2 = int(center[1] - t * dx)

    # Ensure indices are within bounds
    if 0 <= x1 < 100 and 0 <= y1 < 100:
        cross_profile.append(array[y1, x1])  # First diagonal
    if 0 <= x2 < 100 and 0 <= y2 < 100:
        cross_profile.append(array[y2, x2])  # Second diagonal

# Convert to a NumPy array
cross_profile = np.array(cross_profile)

# Display the cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile at 25 Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
