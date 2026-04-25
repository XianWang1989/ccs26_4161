
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Define parameters
center = (50, 50)
angle = 25  # in degrees
length = 20  # length of the cross profile

# Convert angle to radians
theta = np.radians(angle)

# Calculate offsets
offset_x = np.arange(-length, length + 1)
offset_y = np.round(np.tan(theta) * offset_x).astype(int)

# Generate coordinates for the cross profile
cross_profile_coords = []
for dx in offset_x:
    for dy in (-1, 0, 1):  # Vertical line part
        x = center[0] + dx
        y = center[1] + dy
        if 0 <= x < 100 and 0 <= y < 100:
            cross_profile_coords.append(array[x, y])
    for dy in offset_y:  # Diagonal line part
        x = center[0] + dx
        y = center[1] + dy
        if 0 <= x < 100 and 0 <= y < 100:
            cross_profile_coords.append(array[x, y])

# Convert to a numpy array
cross_profile = np.array(cross_profile_coords)

# Visualize the original array and the cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Array')
plt.imshow(array, cmap='gray')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Cross Profile')
plt.plot(cross_profile)
plt.xlabel('Sample Points')
plt.ylabel('Intensity')

plt.tight_layout()
plt.show()
