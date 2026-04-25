
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D array
array = np.random.rand(100, 100)

# Parameters
center = (50, 50)
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

# Calculate direction vectors
theta = np.radians(angle)
dx = np.cos(theta)
dy = np.sin(theta)

# Generate points along the cross
points = []

# Horizontal line
for i in range(-length, length + 1):
    x = int(center[0] + i)
    y1 = int(center[1] + dy * i)
    y2 = int(center[1] - dy * i)

    if 0 <= x < 100 and 0 <= y1 < 100:
        points.append(array[y1, x])
    if 0 <= x < 100 and 0 <= y2 < 100:
        points.append(array[y2, x])

# Convert points to a NumPy array
cross_profile = np.array(points)

# Print the result
print(cross_profile)

# Optional: visualize the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter([center[0]] * len(cross_profile), [center[1]] * len(cross_profile), color='red')
plt.title('Original Array with Cross Profile Center')
plt.show()
