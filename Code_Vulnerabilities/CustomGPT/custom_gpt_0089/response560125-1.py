
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Convert angle from degrees to radians
    theta = np.radians(angle)

    # Calculate direction vectors for the cross profile
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Get the center coordinates
    cx, cy = center

    # Generate coordinates for the cross profile
    points = []
    for d in range(-length//2, length//2 + 1):
        x = int(cx + d * dx)
        y = int(cy + d * dy)
        if 0 <= x < array.shape[1] and 0 <= y < array.shape[0]:
            points.append(array[y, x])

    return np.array(points)

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)
angle = 25  # in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.plot(center[0], center[1], 'ro')  # center point
plt.title('Original Array with Center Point')
plt.show()

plt.plot(cross_profile)
plt.title('Cross Profile at 25 Degrees')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.grid()
plt.show()
