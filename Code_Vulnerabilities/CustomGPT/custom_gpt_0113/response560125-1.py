
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array_size = 100
array = np.random.rand(array_size, array_size)

# Function to extract a diagonal cross profile
def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate the direction of the diagonal
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Initialize coordinates for the cross profile
    coordinates = []

    for i in range(-length // 2, length // 2 + 1):
        x1 = int(x_center + i * dx)
        y1 = int(y_center + i * dy)

        x2 = int(x_center + i * dy)  # Perpendicular direction
        y2 = int(y_center - i * dx

        # Check bounds
        if 0 <= x1 < array_size and 0 <= y1 < array_size:
            coordinates.append(array[y1, x1])

        if 0 <= x2 < array_size and 0 <= y2 < array_size:
            coordinates.append(array[y2, x2])

    return np.array(coordinates)

# Parameters
center = (50, 50)
angle = 25
length = 20

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()
plt.show()

plt.plot(cross_profile, marker='o')
plt.title('Diagonal Cross Profile')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
