
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array as an example
array = np.random.rand(100, 100)

# Function to extract diagonal cross profile
def extract_cross_profile(arr, center, angle, length=20):
    angle_rad = np.radians(angle)
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    x, y = center
    cross_points = []

    for i in range(-length, length + 1):
        # Calculate coordinates for the cross profile points
        x1 = int(x + i * dy)
        y1 = int(y + i * dx)
        x2 = int(x + i * dx)
        y2 = int(y + i * dy)

        # Collect values if within bounds
        if 0 <= x1 < arr.shape[0] and 0 <= y1 < arr.shape[1]:
            cross_points.append(arr[x1, y1])

        if 0 <= x2 < arr.shape[0] and 0 <= y2 < arr.shape[1]:
            cross_points.append(arr[x2, y2])

    return cross_points

# Extract cross profile
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Plotting the original array and its cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()
plt.show()

plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Profile Points')
plt.ylabel('Value')
plt.show()
