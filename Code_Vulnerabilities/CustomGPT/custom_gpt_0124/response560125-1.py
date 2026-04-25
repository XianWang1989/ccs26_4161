
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    """Extract a diagonal cross profile from a 2D NumPy array."""
    cx, cy = center
    theta = np.radians(angle)

    # Calculate the direction vectors for the cross profile
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Calculate coordinates for the cross profile
    points = []
    for t in range(-length, length + 1):
        # Calculate the x and y offsets
        x1 = int(cx + t * dy)
        y1 = int(cy + t * dx)
        x2 = int(cx + t * -dy)
        y2 = int(cy + t * -dx)

        # Store valid points
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            points.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            points.append(array[x2, y2])

    return np.array(points)

# Example usage
array = np.random.rand(100, 100)
center = (50, 50)
angle = 25
length = 20
cross_profile = extract_cross_profile(array, center, angle, length)

# Visualizing the original array and cross profile
plt.imshow(array, cmap='gray', interpolation='nearest')
plt.title('2D NumPy Array')
plt.colorbar()

plt.figure()
plt.plot(cross_profile)
plt.title('Extracted Cross Profile')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.grid()
plt.show()
