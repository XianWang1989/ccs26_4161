
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    cross_profile = []

    # Convert angle to radians
    theta = np.radians(angle)

    # Create a line based on the angle
    for d in range(-length // 2, length // 2 + 1):
        x1 = int(center[0] + d * np.cos(theta))
        y1 = int(center[1] + d * np.sin(theta))
        x2 = int(center[0] + d * np.cos(theta + np.pi))
        y2 = int(center[1] + d * np.sin(theta + np.pi))

        # Check if points are within array bounds and collect them
        if 0 <= x1 < rows and 0 <= y1 < cols:
            cross_profile.append(array[x1, y1])

        if 0 <= x2 < rows and 0 <= y2 < cols:
            cross_profile.append(array[x2, y2])

    return cross_profile

# Example usage
array = np.random.rand(100, 100)  # Create a sample 100x100 array
center = (50, 50)
angle = 25  # in degrees
length = 20  # length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting for visualization
plt.plot(cross_profile)
plt.title(f'Cross Profile at {angle} degrees')
plt.xlabel('Distance along cross profile')
plt.ylabel('Value')
plt.show()
