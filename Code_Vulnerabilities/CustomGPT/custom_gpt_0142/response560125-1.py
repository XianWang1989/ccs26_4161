
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 NumPy array
array = np.random.rand(100, 100)

# Function to extract the diagonal cross profile
def extract_cross_profile(array, center, angle, length=20):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)

    cross_points = []

    # Calculate the offsets for the cross profile
    for offset in range(-length, length + 1):
        # Calculate coordinates for the diagonal line
        x1 = int(x_center + offset * np.cos(angle_rad))
        y1 = int(y_center + offset * np.sin(angle_rad))

        # Calculate coordinates for the perpendicular line
        x2 = int(x_center + offset * np.cos(angle_rad + np.pi / 2))
        y2 = int(y_center + offset * np.sin(angle_rad + np.pi / 2))

        # Append the points to the cross profile list if they are within boundaries
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_points.append(array[x1, y1])

        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_points.append(array[x2, y2])

    return np.array(cross_points)

# Define center and angle
center = (50, 50)
angle = 25

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle)

# Print the result and visualize the original array and cross profile
print("Extracted Cross Profile:", cross_profile)

# Optional: Visualize the original array
plt.imshow(array, cmap='gray')
plt.scatter([center[1]], [center[0]], color='red')  # center point
plt.title('Original Array with Center Point')
plt.show()
