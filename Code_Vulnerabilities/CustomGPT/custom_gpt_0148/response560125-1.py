
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.random((100, 100))

# Function to extract cross profile
def extract_cross_profile(arr, center, angle, length):
    y, x = center
    angle_rad = np.radians(angle)

    # Calculate direction vectors
    dy = np.sin(angle_rad)
    dx = np.cos(angle_rad)

    # Calculate the cross points
    cross_points = []
    for d in range(-length, length + 1):
        # Points on the angle
        point1 = (int(y + d * dy), int(x + d * dx))
        point2 = (int(y - d * dy), int(x - d * dx))

        # Check bounds and add points
        if 0 <= point1[0] < arr.shape[0] and 0 <= point1[1] < arr.shape[1]:
            cross_points.append(arr[point1])
        if 0 <= point2[0] < arr.shape[0] and 0 <= point2[1] < arr.shape[1]:
            cross_points.append(arr[point2])

    return cross_points

# Extract cross profile centered at (50, 50) at a 25-degree angle
cross_length = 50  # Length of the cross profile
cross_profile = extract_cross_profile(array, (50, 50), 25, cross_length)

# Display the array and extracted profile
plt.imshow(array, cmap='gray')
plt.title('100x100 Array')
plt.scatter([50], [50], color='red')  # Mark the center point
plt.show()

print("Extracted Cross Profile:", cross_profile)
