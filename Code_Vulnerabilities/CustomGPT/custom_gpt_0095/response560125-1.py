
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 sample 2D array
array = np.random.rand(100, 100)

# Function to extract diagonal cross profile
def extract_cross_profile(array, center, angle_deg, length):
    angle_rad = np.radians(angle_deg)
    x_center, y_center = center

    # Calculate diagonal offsets
    x_offset = np.cos(angle_rad)
    y_offset = np.sin(angle_rad)

    # Create arrays to hold the cross profile coordinates
    cross_coords = []

    # Iterate through the length of the cross
    for i in range(-length, length + 1):
        x1 = int(x_center + i * y_offset)
        y1 = int(y_center + i * x_offset)
        x2 = int(x_center + i * (-y_offset))
        y2 = int(y_center + i * (-x_offset))

        # Append valid coordinates to the list
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_coords.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_coords.append(array[x2, y2])

    return np.array(cross_coords)

# Parameters
center = (50, 50)
angle = 25  # degrees
length = 25  # length of the cross

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Array')
plt.imshow(array, cmap='viridis')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Cross Profile')
plt.plot(cross_profile)
plt.xlabel('Profile Index')
plt.ylabel('Value')

plt.tight_layout()
plt.show()
