
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle_degrees, length):
    angle_radians = np.radians(angle_degrees)
    x0, y0 = center
    dx = np.cos(angle_radians)
    dy = np.sin(angle_radians)

    # Generate the coordinates
    coords = []
    for i in range(-length//2, length//2 + 1):
        x = int(x0 + i * dx)
        y = int(y0 + i * dy)
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            coords.append(array[x, y])

    return np.array(coords)

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 50  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Plotting the cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Points along the cross profile')
plt.ylabel('Values')
plt.grid()
plt.show()
