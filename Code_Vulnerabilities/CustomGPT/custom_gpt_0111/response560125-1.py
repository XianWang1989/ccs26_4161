
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate direction vectors
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Create the line points
    points = []
    for i in range(-length//2, length//2 + 1):
        x = int(x_center + i * dx)
        y = int(y_center + i * dy)
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            points.append(array[y, x])

    return np.array(points)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile
center = (50, 50)
angle = 25
length = 100  # Length of the cross profile to extract
cross_profile = extract_cross_profile(array, center, angle, length)

# Display the original array and the cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.scatter([center[0]], [center[1]], color='red')  # Mark the center

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Cross Profile at 25 Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Value')

plt.tight_layout()
plt.show()
