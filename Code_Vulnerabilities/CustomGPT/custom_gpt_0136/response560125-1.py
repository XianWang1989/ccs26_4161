
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=20):
    # Calculate the change in x and y based on the angle
    radians = np.deg2rad(angle)
    dx = np.cos(radians)
    dy = np.sin(radians)

    # Get the center point
    x0, y0 = center

    # Generate points along the diagonal
    x_points = []
    y_points = []

    for i in range(-length, length + 1):
        x = int(x0 + i * dx)
        y = int(y0 + i * dy)
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            x_points.append(x)
            y_points.append(y)

    # Extract values from the array
    profile = array[x_points, y_points]
    return profile

# Example usage
array = np.random.rand(100, 100)
center = (50, 50)
angle = 25

cross_profile = extract_cross_profile(array, center, angle)

# Plotting the cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Distance along diagonal')
plt.ylabel('Values')
plt.show()
