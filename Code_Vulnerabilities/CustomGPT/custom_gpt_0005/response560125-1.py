
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

def extract_cross_profile(array, center, angle_degrees, length=20):
    angle_radians = np.radians(angle_degrees)

    # Calculate offsets for the cross profile
    x_offsets = np.arange(-length, length + 1)
    y_offsets = np.arange(-length, length + 1)

    # Calculate coordinates for diagonal profile
    x_diag = center[0] + x_offsets * np.cos(angle_radians) - y_offsets * np.sin(angle_radians)
    y_diag = center[1] + x_offsets * np.sin(angle_radians) + y_offsets * np.cos(angle_radians)

    # Extract values; clip to stay within the array bounds
    x_diag = np.clip(x_diag, 0, array.shape[0] - 1).astype(int)
    y_diag = np.clip(y_diag, 0, array.shape[1] - 1).astype(int)

    return array[x_diag, y_diag]

# Center of the cross profile
center = (50, 50)
angle = 25

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle)

# Display the original array and the profile
plt.subplot(1, 2, 1)
plt.title('Original Array')
plt.imshow(array, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Diagonal Cross Profile')
plt.plot(cross_profile)
plt.xlabel('Index')
plt.ylabel('Value')

plt.show()
