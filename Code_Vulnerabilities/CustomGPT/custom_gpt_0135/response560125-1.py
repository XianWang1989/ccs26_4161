
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Define the center point and angle
center = (50, 50)
angle = 25  # degrees

# Calculate the slope of the lines
slope = np.tan(np.radians(angle))

# Define the length of the cross arms
length = 25

# Determine coordinates for the cross profile
coordinates = []

# Create points for the diagonal lines
for i in range(-length, length + 1):
    x1 = center[0] + i
    y1 = center[1] + slope * i
    x2 = center[0] + i
    y2 = center[1] - slope * i

    # Ensure indices are within array bounds
    if 0 <= x1 < 100 and 0 <= y1 < 100:
        coordinates.append(array[x1, int(y1)])
    if 0 <= x2 < 100 and 0 <= y2 < 100:
        coordinates.append(array[x2, int(y2)])

# Convert to a numpy array for easier manipulation
cross_profile = np.array(coordinates)

# Display the original array for visualization (optional)
plt.imshow(array, cmap='viridis')
plt.scatter([center[0]] * len(cross_profile), range(len(cross_profile)), color='red', label='Cross Profile Points')
plt.title('Original Array with Cross Profile Points')
plt.legend()
plt.colorbar()
plt.show()

# Output the cross profile
print("Cross Profile:", cross_profile)
