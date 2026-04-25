
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array_size = 100
array = np.random.rand(array_size, array_size)

# Center and angle
center = (50, 50)
angle = 25  # degrees

# Convert angle to radians
theta = np.radians(angle)

# Create offsets for both directions
length = 40  # how far to extend the cross from the center
x_offsets = np.arange(-length, length + 1)
y_offsets = np.tan(theta) * x_offsets

# Calculate points for the diagonal cross
x1 = center[0] + x_offsets.astype(int)
y1 = center[1] + y_offsets.astype(int)

# Clip to array bounds
valid_indices = (x1 >= 0) & (x1 < array_size) & (y1 >= 0) & (y1 < array_size)
diagonal_cross = array[x1[valid_indices], y1[valid_indices]]

# Show the original array and the extracted profile
plt.subplot(1, 2, 1)
plt.title("Original Array")
plt.imshow(array, cmap='gray')
plt.scatter(center[0], center[1], color='red')  # Mark the center

plt.subplot(1, 2, 2)
plt.title("Diagonal Cross Profile")
plt.plot(diagonal_cross, marker='o')
plt.xlabel("Profile Index")
plt.ylabel("Value")
plt.grid()

plt.tight_layout()
plt.show()
