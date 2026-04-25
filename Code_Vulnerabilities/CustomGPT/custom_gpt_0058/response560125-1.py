
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

# Center point
center_x, center_y = 50, 50

# Angle in degrees
angle_degrees = 25
angle_radians = np.radians(angle_degrees)

# Length of the cross arms
length = 30

# Calculate the offsets for the diagonal cross
x_offsets = np.array([-length, 0, length, 0])  # Horizontal points
y_offsets = np.array([0, -length, 0, length])  # Vertical points

# Create the cross points at the specified angle
cross_points = []
for x_offset, y_offset in zip(x_offsets, y_offsets):
    rotated_x = center_x + (x_offset * np.cos(angle_radians) - y_offset * np.sin(angle_radians))
    rotated_y = center_y + (x_offset * np.sin(angle_radians) + y_offset * np.cos(angle_radians))
    cross_points.append((int(rotated_x), int(rotated_y)))

# Get the values from the original array
cross_values = []
for point in cross_points:
    x, y = point
    if 0 <= x < 100 and 0 <= y < 100:  # Check bounds
        cross_values.append(array[y, x])

# Print the extracted values
print("Cross profile values at angle 25 degrees:", cross_values)

# Optional: Visualize the original array and the cross points
plt.imshow(array, cmap='gray')
plt.scatter([p[0] for p in cross_points], [p[1] for p in cross_points], color='red')
plt.title('Cross Profile at 25 Degrees')
plt.show()
