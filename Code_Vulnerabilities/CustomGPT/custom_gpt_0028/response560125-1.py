
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    x_center, y_center = center

    # Calculate the endpoints of the diagonal line
    theta = np.radians(angle)
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    coords = []

    # Collect coordinates along the diagonal
    for offset in range(-length // 2, length // 2 + 1):
        x1 = int(x_center + offset * dy)
        y1 = int(y_center + offset * dx)
        x2 = int(x_center - offset * dy)
        y2 = int(y_center - offset * dx)

        # Check bounds and append values to the list
        if 0 <= x1 < rows and 0 <= y1 < cols:
            coords.append(array[x1, y1])
        if 0 <= x2 < rows and 0 <= y2 < cols:
            coords.append(array[x2, y2])

    return np.array(coords)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)                  # Center of the cross profile
angle = 25                         # Angle in degrees
length = 20                        # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting for visualization
plt.figure(figsize=(10, 5))
plt.plot(cross_profile)
plt.title(f'Cross Profile at {angle} degrees')
plt.xlabel('Offset')
plt.ylabel('Value')
plt.grid()
plt.show()
