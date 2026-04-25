
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    cross_points = []

    # Calculate the angle in radians
    theta = np.radians(angle)

    # Calculate the offsets based on length along both diagonal directions
    for d in range(-length, length + 1):
        # Calculate the x and y offsets for the two diagonals
        x_offset1 = int(d * np.cos(theta))
        y_offset1 = int(d * np.sin(theta))
        x_offset2 = int(-d * np.cos(theta))
        y_offset2 = int(-d * np.sin(theta))

        # Compute the coordinates for both ends of the cross
        point1 = (center[0] + x_offset1, center[1] + y_offset1)
        point2 = (center[0] + x_offset2, center[1] + y_offset2)

        # Append the points, ensuring we are within array bounds
        if 0 <= point1[0] < array.shape[0] and 0 <= point1[1] < array.shape[1]:
            cross_points.append(array[point1[0], point1[1]])
        if 0 <= point2[0] < array.shape[0] and 0 <= point2[1] < array.shape[1]:
            cross_points.append(array[point2[0], point2[1]])

    return np.array(cross_points)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile centered at (50, 50) with a 25-degree angle and length of 20
cross_profile = extract_cross_profile(array, (50, 50), 25, 20)

# Print the extracted cross profile
print(cross_profile)

# Optional: visualize the original array and the extraction point
plt.imshow(array, cmap='gray')
plt.scatter(50, 50, color='red')  # center point
plt.title("Original Array with Center Point")
plt.show()
