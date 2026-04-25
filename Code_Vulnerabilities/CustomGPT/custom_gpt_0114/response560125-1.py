
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=50):
    # Convert angle to radians
    theta = np.radians(angle)

    # Create a list to hold the points in the cross profile
    cross_profile = []

    # Calculate step sizes
    dx = np.cos(theta)
    dy = np.sin(theta)

    for i in range(-length, length):
        # Calculate the coordinates based on the angle
        x1 = center[0] + i * dx
        y1 = center[1] + i * dy

        # Calculate the coordinates for the perpendicular direction
        x2 = center[0] - i * dy
        y2 = center[1] + i * dx

        # Append the points to the profile (ensure they are in bounds)
        if 0 <= int(x1) < array.shape[0] and 0 <= int(y1) < array.shape[1]:
            cross_profile.append(array[int(x1), int(y1)])

        if 0 <= int(x2) < array.shape[0] and 0 <= int(y2) < array.shape[1]:
            cross_profile.append(array[int(x2), int(y2)])

    return np.array(cross_profile)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees

profile = extract_cross_profile(array, center, angle)

# Plot the original array and the cross profile
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('2D Array')

plt.subplot(1, 2, 2)
plt.plot(profile)
plt.title('Cross Profile')
plt.xlabel('Sample Points')
plt.ylabel('Value')

plt.tight_layout()
plt.show()
