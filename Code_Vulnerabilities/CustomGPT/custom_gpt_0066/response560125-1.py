
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Parameters
center = (50, 50)  # Center point
angle = 25         # Angle in degrees
length = 20        # Length of the cross profile

# Convert angle to radians
theta = np.radians(angle)

# Calculate offsets
dx = length * np.cos(theta)
dy = length * np.sin(theta)

# Create the coordinates for the cross profile
x1 = int(center[0] + dx)
y1 = int(center[1] + dy)
x2 = int(center[0] - dx)
y2 = int(center[1] - dy)

# Extract the profile
cross_profile = []
for x in range(x2, x1 + 1):
    if 0 <= x < 100:
        y = int(center[1] + ((x - center[0]) * dy / dx))
        if 0 <= y < 100:
            cross_profile.append(array[y, x])

# Convert cross profile to a numpy array
cross_profile = np.array(cross_profile)

# Display the results
print("Cross Profile Values:", cross_profile)

# Optional: Visualize the array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter([x1, x2], [y1, y2], color='red')  # Marking ends of diagonal
plt.title('2D Array with Cross Profile Points')
plt.show()
