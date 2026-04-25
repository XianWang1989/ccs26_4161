
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.random((100, 100))

def extract_cross_profile(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    # Calculate the direction vectors
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Initialize lists to collect the points
    points = []

    # Generate points along the cross
    for i in range(-length//2, length//2 + 1):
        # Calculate diagonal points
        x1 = int(x_center + i * dx)
        y1 = int(y_center + i * dy)
        x2 = int(x_center - i * dx)
        y2 = int(y_center - i * dy)

        # Collect values within bounds
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            points.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            points.append(array[x2, y2])

    return points

# Center of the cross, angle in degrees, and profile length
center = (50, 50)
angle = 25
length = 50

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Display the results
plt.plot(cross_profile)
plt.title(f'Cross Profile at {angle}°')
plt.xlabel('Point Index')
plt.ylabel('Value')
plt.show()
