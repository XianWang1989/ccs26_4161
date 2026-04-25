
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 2D array
array_size = 100
array = np.random.rand(array_size, array_size)

# Parameters
center = (50, 50)
angle = 25  # degrees

# Convert angle to radians
angle_rad = np.radians(angle)

# Calculate the length of the cross profile
length = array_size // 2

# Calculate coordinates
x1 = center[0] - length * np.cos(angle_rad)
y1 = center[1] - length * np.sin(angle_rad)
x2 = center[0] + length * np.cos(angle_rad)
y2 = center[1] + length * np.sin(angle_rad)

# Get the diagonal cross profile
cross_profile = []
for i in range(-length, length):
    x = int(center[0] + i * np.cos(angle_rad))
    y = int(center[1] + i * np.sin(angle_rad))
    if 0 <= x < array_size and 0 <= y < array_size:
        cross_profile.append(array[y, x])

# Convert the list to a NumPy array for easy handling
cross_profile = np.array(cross_profile)

# Plotting the original array and the cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.scatter(center[0], center[1], color='red')  # Center point

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile at 25 Degrees')
plt.xlabel('Offset')
plt.ylabel('Value')
plt.grid()
plt.show()
