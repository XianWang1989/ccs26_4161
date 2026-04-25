
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Function to extract diagonal cross profile
def extract_cross_profile(array, center, angle, length=20):
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate offsets
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Points along the cross profile
    points = []
    for i in range(-length, length + 1):
        x1 = int(x_center + i * dy)  # Vertical line
        y1 = int(y_center + i * dx
        points.append((x1, y1))

        x2 = int(x_center - i * dy)  # Horizontal line
        y2 = int(y_center - i * dx)
        points.append((x2, y2))

    # Extract values from the array and filter valid points
    values = []
    for x, y in points:
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            values.append(array[x, y])

    return np.array(values)

# Center point and angle
center = (50, 50)
angle = 25
profile = extract_cross_profile(array, center, angle)

# Display the result
print("Extracted Cross Profile:", profile)

# Optional: Visualize the array and cross profile
plt.imshow(array, cmap='gray')
plt.title('2D Array and Cross Profile')
plt.colorbar()
plt.scatter([center[1]], [center[0]], color='red')  # Center point
plt.show()
