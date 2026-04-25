
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    rad_angle = np.radians(angle)

    # Generate the indices for the cross profile
    offsets = np.arange(-length // 2, length // 2 + 1)
    x_offsets = offsets * np.cos(rad_angle) + x_center
    y_offsets = offsets * np.sin(rad_angle) + y_center

    # Round the indices and retrieve values
    x_indices = np.clip(np.round(x_offsets).astype(int), 0, array.shape[0] - 1)
    y_indices = np.clip(np.round(y_offsets).astype(int), 0, array.shape[1] - 1)

    return array[x_indices, y_indices]

# Parameters
center = (50, 50)
angle = 25
length = 40  # Length of the cross profile

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the cross profile
plt.imshow(array, cmap='gray', interpolation='nearest')
plt.scatter([center[0]], [center[1]], color='red')  # center point
plt.title('Original Array')
plt.colorbar()
plt.show()

plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Offset')
plt.ylabel('Value')
plt.grid()
plt.show()
