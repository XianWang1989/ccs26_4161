
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Convert angle from degrees to radians
    theta = np.radians(angle)

    # Calculate direction vectors for the line
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Create profiles
    profile = []

    for i in range(-length, length + 1):
        x = int(center[0] + i * dx)
        y = int(center[1] + i * dy)

        # Ensure that the indices are within bounds
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile.append(array[x, y])

    return np.array(profile)

# Example usage:
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Visualize the original array and the extracted cross profile
plt.imshow(array, cmap='gray', interpolation='nearest')
plt.title('Original 2D Array')
plt.colorbar()
plt.show()

# Plot the cross profile
plt.plot(cross_profile)
plt.title('Extracted Cross Profile')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid()
plt.show()
