
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length=20):
    # Convert angle to radians
    theta = np.radians(angle)

    # Get center coordinates
    x, y = center

    # Calculate dx and dy from the angle
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Create the coordinates for the cross profile
    coords = []
    for shift in range(-length//2, length//2 + 1):
        x1 = int(x + shift * dx - (dy * shift))
        y1 = int(y + shift * dy + (dx * shift))
        if 0 <= x1 < arr.shape[0] and 0 <= y1 < arr.shape[1]:
            coords.append(arr[x1, y1])

    return np.array(coords)

# Create a 100x100 array with random values
array_2d = np.random.rand(100, 100)

# Extracting the cross profile
cross_profile = extract_cross_profile(array_2d, (50, 50), 25, length=40)

# Plotting the cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
