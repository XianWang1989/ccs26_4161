
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array_size = 100
array = np.random.rand(array_size, array_size)

# Function to extract diagonal cross profile
def extract_diagonal_cross(array, center, angle, length):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate the direction of the diagonal
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Generate the coordinates for the cross profile
    coords = []
    for i in range(-length, length + 1):
        x1 = int(x_center + i * dx)
        y1 = int(y_center + i * dy)
        coords.append((x1, y1))

    # Get values from the array at the computed coordinates
    values = []
    for x, y in coords:
        if 0 <= x < array_size and 0 <= y < array_size:
            values.append(array[y, x])  # Note: array[y, x] for row-major order
        else:
            values.append(np.nan)  # Handle out-of-bounds with NaN

    return np.array(values)

# Define parameters
center = (50, 50)
angle = 25
length = 20

# Extract the cross profile
cross_profile = extract_diagonal_cross(array, center, angle, length)

# Plotting for visualization
plt.imshow(array, cmap='gray')
plt.colorbar()
plt.scatter([center[0]], [center[1]], color='red')  # Center point
plt.title('2D Array with Center Point')
plt.show()

# Show the extracted cross profile
print("Diagonal Cross Profile:", cross_profile)
