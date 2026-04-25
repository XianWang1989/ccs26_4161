
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=10):
    """Extracts a diagonal cross profile from a 2D NumPy array."""
    rows, cols = array.shape
    x_center, y_center = center

    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate direction vectors
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Generate points for cross profile
    points = []
    for d in range(-length, length + 1):
        x1 = int(x_center + d * dy)  # Perpendicular direction
        y1 = int(y_center + d * dx)
        x2 = int(x_center - d * dy)  # Opposite direction
        y2 = int(y_center - d * dx)

        # Check bounds
        if 0 <= x1 < rows and 0 <= y1 < cols:
            points.append(array[x1, y1])
        if 0 <= x2 < rows and 0 <= y2 < cols:
            points.append(array[x2, y2])

    return np.array(points)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)
angle = 25

cross_profile = extract_cross_profile(array, center, angle)

# Plot the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.title('Original Array')
plt.colorbar()
plt.show()

plt.plot(cross_profile, marker='o')
plt.title('Cross Profile')
plt.xlabel('Profile Points')
plt.ylabel('Value')
plt.show()
