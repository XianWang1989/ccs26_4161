
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array filled with random values
array = np.random.rand(100, 100)

def extract_diagonal_cross(array, center, angle, length):
    rows, cols = array.shape
    x_center, y_center = center
    angle_rad = np.radians(angle)

    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    cross_profile = []

    # Create the cross profile
    for d in range(-length, length + 1):
        # Calculate coordinates for one diagonal
        x1 = int(x_center + d * dx)
        y1 = int(y_center + d * dy)
        x2 = int(x_center + d * -dy)  # Perpendicular diagonal
        y2 = int(y_center + d * dx)

        # Check bounds and append values
        if 0 <= x1 < rows and 0 <= y1 < cols:
            cross_profile.append(array[x1, y1])
        if 0 <= x2 < rows and 0 <= y2 < cols:
            cross_profile.append(array[x2, y2])

    return cross_profile

# Example usage
center = (50, 50)
angle = 25
length = 25 # half-length of the cross profile
cross_data = extract_diagonal_cross(array, center, angle, length)

# Optional: Plot the original array and the cross profile
plt.imshow(array, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Original Array')
plt.show()

plt.plot(cross_data)
plt.title('Diagonal Cross Profile')
plt.xlabel('Position along diagonal')
plt.ylabel('Value')
plt.show()
