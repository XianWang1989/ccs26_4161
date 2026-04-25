
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Define the function to extract the diagonal cross profile
def extract_cross_profile(array, center, angle, length=50):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate the direction of the cross profile
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    profile = []

    for d in range(-length, length+1):
        x = int(x_center + d * dx)
        y = int(y_center + d * dy)

        # Ensure indices are within bounds
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile.append(array[x, y])

    return np.array(profile)

# Extract the cross profile
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Visualize the original array and the cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Cross Profile at 25 Degrees')
plt.xlabel('Distance from Center')
plt.ylabel('Value')
plt.grid()
plt.show()
