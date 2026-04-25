
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Parameters
center = (50, 50)  # Center of the cross profile
angle = 25         # Angle in degrees

# Convert angle to radians
angle_rad = np.deg2rad(angle)

# Calculate the direction vectors
dx = np.cos(angle_rad)
dy = np.sin(angle_rad)

# Length of the cross profile (adjust as needed)
length = 40

# Extract the points along the cross profile
x_cross = []
y_cross = []

for i in range(-length, length + 1):
    x1 = int(center[0] + i * dx)
    y1 = int(center[1] + i * dy)
    x2 = int(center[0] - i * dx)
    y2 = int(center[1] - i * dy)

    if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
        x_cross.append(x1)
        y_cross.append(y1)
    if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
        x_cross.append(x2)
        y_cross.append(y2)

# Create a mask to extract the cross values
cross_profile = []
for x, y in zip(x_cross, y_cross):
    cross_profile.append(array[y, x])

# Convert to a NumPy array
cross_profile = np.array(cross_profile)

# Optional: Visualize the array and the cross profile
plt.imshow(array, cmap='viridis')
plt.scatter(x_cross, y_cross, color='red', s=1)
plt.title('Cross Profile Visualization')
plt.colorbar()
plt.show()

# Output the cross profile
print("Cross Profile Values:", cross_profile)
