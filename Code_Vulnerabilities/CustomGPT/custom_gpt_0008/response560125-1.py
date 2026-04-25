
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    rows, cols = arr.shape
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate increments
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Generate points for the cross profile
    x1 = int(x_center - dx), int(x_center + dx)
    y1 = int(y_center - dy), int(y_center + dy)

    # Ensure points are within bounds
    idxs1 = [(y1[0], x1[0]), (y1[1], x1[1])]
    idxs2 = [(y_center - dx, x_center + dy), (y_center + dx, x_center - dy)]

    points = []
    for (y1, x1), (y2, x2) in zip(idxs1, idxs2):
        # Line plotting using Bresenham's algorithm
        points.extend(bresenham(x1, y1, x2, y2))

    # Extract values from the array
    cross_values = arr[np.array(points)[:,0], np.array(points)[:,1]]

    return cross_values

def bresenham(x1, y1, x2, y2):
    """Bresenham's Line Algorithm to generate points between two points."""
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((y1, x1))
        if x1 == x2 and y1 == y2:
            break
        err2 = err * 2
        if err2 > -dy:
            err -= dy
            x1 += sx
        if err2 < dx:
            err += dx
            y1 += sy
    return points

# Example usage
arr = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)

# Visualizing the result
plt.imshow(arr, cmap='gray')
plt.scatter([center[1]], [center[0]], color='red')  # Center point
plt.title("2D Array with Center Point")
plt.show()

print(cross_profile)
