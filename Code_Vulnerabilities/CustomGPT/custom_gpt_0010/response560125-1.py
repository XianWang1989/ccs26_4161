
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=20):
    x0, y0 = center
    theta = np.radians(angle)

    # Calculate the offsets based on the angle
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Initialize the cross profile
    profile = []

    for i in range(-length, length + 1):
        x = int(x0 + i * dy)
        y = int(y0 + i * dx)
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            profile.append(array[x, y])

    return np.array(profile)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile centered at (50, 50) with a 25-degree angle
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle)

# Plotting the result
plt.plot(cross_profile)
plt.title('Cross Profile')
plt.xlabel('Position along the cross line')
plt.ylabel('Value')
plt.grid()
plt.show()
