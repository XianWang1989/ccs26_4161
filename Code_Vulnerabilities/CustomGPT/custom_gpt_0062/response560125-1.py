
import numpy as np

# Create a 100x100 array
array = np.random.rand(100, 100)

# Parameters
center = (50, 50)
angle = 25  # degrees

# Convert angle to radians
theta = np.radians(angle)

# Calculate the offsets for the cross profile
length = 30  # Length of the cross profile
dx = np.round(length * np.cos(theta)).astype(int)
dy = np.round(length * np.sin(theta)).astype(int)

# Create lists to store the diagonal coordinates
coords = []

# Extract the diagonal cross profile
for i in range(-length, length + 1):
    x1 = center[0] + i
    y1 = center[1] + (i * dy) // dx
    x2 = center[0] + i
    y2 = center[1] - (i * dy) // dx

    # Add the coordinates to the list
    if 0 <= x1 < 100 and 0 <= y1 < 100:
        coords.append(array[x1, y1])
    if 0 <= x2 < 100 and 0 <= y2 < 100:
        coords.append(array[x2, y2])

# Convert the list to a NumPy array
cross_profile = np.array(coords)

print(cross_profile)
