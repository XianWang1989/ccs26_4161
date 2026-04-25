
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    # Create a grid of points for the cross profile
    x, y = np.meshgrid(np.arange(-length, length + 1), np.arange(-length, length + 1))

    # Rotate the points based on the angle
    theta = np.radians(angle)
    x_rotated = np.cos(theta) * x - np.sin(theta) * y
    y_rotated = np.sin(theta) * x + np.cos(theta) * y

    # Center the diagonal cross profile
    centered_x = center[0] + x_rotated
    centered_y = center[1] + y_rotated

    # Extract the values from the array, ensuring coordinates are within bounds
    profile = []
    for xi, yi in zip(centered_x.flatten(), centered_y.flatten()):
        if 0 <= xi < arr.shape[0] and 0 <= yi < arr.shape[1]:
            profile.append(arr[int(xi), int(yi)])

    return np.array(profile)

# Example usage
arr = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)                # Center at (50,50)
angle = 25                       # Angle 25 degrees
length = 20                      # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)

# Plot the original array and cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Array')
plt.imshow(arr, cmap='viridis')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Cross Profile')
plt.plot(cross_profile)
plt.xlabel('Profile Index')
plt.ylabel('Value')

plt.tight_layout()
plt.show()
