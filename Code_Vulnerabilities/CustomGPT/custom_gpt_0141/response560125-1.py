
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Define the center of the cross
center = (50, 50)

# Define the angle in degrees
angle = 25
angle_rad = np.deg2rad(angle)

# Define the length of the cross profile (you can adjust this)
length = 50

# Compute the coordinates for the diagonal lines
x1 = center[0] + np.arange(-length, length + 1) * np.cos(angle_rad)
y1 = center[1] + np.arange(-length, length + 1) * np.sin(angle_rad)

x2 = center[0] + np.arange(-length, length + 1) * np.cos(angle_rad + np.pi / 2)
y2 = center[1] + np.arange(-length, length + 1) * np.sin(angle_rad + np.pi / 2)

# Round to nearest integer values for indexing
x1 = np.clip(np.round(x1).astype(int), 0, array.shape[0] - 1)
y1 = np.clip(np.round(y1).astype(int), 0, array.shape[1] - 1)

x2 = np.clip(np.round(x2).astype(int), 0, array.shape[0] - 1)
y2 = np.clip(np.round(y2).astype(int), 0, array.shape[1] - 1)

# Extract the values along the two diagonals
cross_profile = array[y1, x1].tolist() + array[y2, x2].tolist()

# Print the extracted cross profile
print("Extracted Cross Profile:")
print(cross_profile)

# Optional: Display the original array and the profile for visualization
plt.imshow(array, cmap='hot', interpolation='nearest')
plt.plot(x1, y1, color='blue', label='Diagonal 1', linewidth=2)
plt.plot(x2, y2, color='green', label='Diagonal 2', linewidth=2)
plt.scatter(center[1], center[0], color='red')  # Mark the center
plt.legend()
plt.title('Cross Profile Extraction')
plt.show()
