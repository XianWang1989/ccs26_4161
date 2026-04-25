
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle_degrees, length):
    # Convert angle to radians
    angle_radians = np.radians(angle_degrees)

    # Create the line coordinates based on the angle
    x_offset = np.cos(angle_radians)
    y_offset = np.sin(angle_radians)

    # Calculate the coordinates of the cross profile
    x_coords = []
    y_coords = []

    for i in range(-length, length + 1):
        x = int(center[0] + i * x_offset)
        y = int(center[1] + i * y_offset)
        if 0 <= x < array.shape[0] and 0 <= y < array.shape[1]:
            x_coords.append(x)
            y_coords.append(y)

    # Extract the values along the diagonal line
    cross_profile = array[x_coords, y_coords]

    return cross_profile

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center_point = (50, 50)           # Center at (50, 50)
angle = 25                         # Angle in degrees
length = 50                        # Length of the cross profile

cross_profile = extract_cross_profile(array, center_point, angle, length)

# Optionally, visualize the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter(center_point[0], center_point[1], color='red')  # Marking the center
plt.plot([center_point[0] + (i * np.cos(np.radians(angle))) for i in range(-length, length + 1)],
         [center_point[1] + (i * np.sin(np.radians(angle))) for i in range(-length, length + 1)],
         color='blue')  # Visualizing the cross profile line
plt.title('Cross Profile Extraction')
plt.show()

print("Cross Profile:", cross_profile)
