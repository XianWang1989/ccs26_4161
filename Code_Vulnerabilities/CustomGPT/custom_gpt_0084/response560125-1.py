
import numpy as np
import matplotlib.pyplot as plt

def extract_diagonal_cross_profile(array, center, angle, length):
    # Create coordinates centered at `center`
    rows, cols = array.shape
    x_center, y_center = center

    # Convert angle from degrees to radians
    theta = np.radians(angle)

    # Calculate the direction vector based on the angle
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Extract points along the diagonals
    points = []
    for d in range(-length, length + 1):
        x1 = int(x_center + d * dy)
        y1 = int(y_center + d * dx)
        if 0 <= x1 < rows and 0 <= y1 < cols:
            points.append(array[x1, y1])

    return np.array(points)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 50  # Half-length of the cross profile

cross_profile = extract_diagonal_cross_profile(array, center, angle, length)

# Plot the cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile at 25 degrees')
plt.xlabel('Distance from center')
plt.ylabel('Value')
plt.show()
