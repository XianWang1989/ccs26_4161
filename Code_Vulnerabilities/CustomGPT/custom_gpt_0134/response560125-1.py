
import numpy as np
import math
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    x_center, y_center = center
    angle_rad = math.radians(angle)

    # Calculate the slope for both directions
    dx = length * math.cos(angle_rad)
    dy = length * math.sin(angle_rad)

    # Points for diagonal lines
    points = [
        (int(x_center + dx), int(y_center + dy)),
        (int(x_center - dx), int(y_center - dy)),
        (int(x_center + dy), int(y_center - dx)),
        (int(x_center - dy), int(y_center + dx))
    ]

    cross_profile = []

    for point in points:
        if 0 <= point[0] < arr.shape[0] and 0 <= point[1] < arr.shape[1]:
            cross_profile.append(arr[point[1], point[0]])

    return np.array(cross_profile)

# Example usage
array_2d = np.random.rand(100, 100)  # Create a random 100x100 array
center_point = (50, 50)
angle = 25  # Angle in degrees
length = 10  # Length from the center point

cross_profile = extract_cross_profile(array_2d, center_point, angle, length)

# Display the results
print(cross_profile)
plt.imshow(array_2d, cmap='gray')
plt.scatter([center_point[0]], [center_point[1]], color='red')  # Center point
plt.title("Cross Profile Extraction")
plt.show()
