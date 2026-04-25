
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    rows, cols = arr.shape
    x0, y0 = center
    angle_rad = np.deg2rad(angle)

    # Calculate the direction vectors
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Calculate the cross profile coordinates
    coordinates = []
    for offset in range(-length // 2, length // 2 + 1):
        x1 = int(x0 + offset * dx)
        y1 = int(y0 + offset * dy)
        if 0 <= x1 < rows and 0 <= y1 < cols:
            coordinates.append(arr[x1, y1])

    return np.array(coordinates)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)
angle = 25
length = 30  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the result
plt.plot(cross_profile)
plt.title('Cross Profile at 25 Degrees')
plt.xlabel('Offset')
plt.ylabel('Value')
plt.show()
