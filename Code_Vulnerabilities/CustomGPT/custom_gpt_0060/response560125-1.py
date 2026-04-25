
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    y_center, x_center = center
    angle_radians = np.radians(angle)

    # Calculate the slope of the cross lines
    slope = np.tan(angle_radians)

    # Create lists to hold the coordinates of the cross profile
    coords = []

    # Diagonal 1 (slope: m)
    for i in range(-length, length + 1):
        y1 = int(y_center + i)
        x1 = int(x_center + slope * i)
        if 0 <= y1 < rows and 0 <= x1 < cols:
            coords.append((y1, x1))

    # Diagonal 2 (slope: -1/m)
    for i in range(-length, length + 1):
        y2 = int(y_center + i)
        x2 = int(x_center - slope * i)
        if 0 <= y2 < rows and 0 <= x2 < cols:
            coords.append((y2, x2))

    return coords

# Example usage:
array = np.random.rand(100, 100)  # Creating a random 100x100 array
center = (50, 50)
angle = 25
length = 20  # Length of the cross profile

cross_profile_indices = extract_cross_profile(array, center, angle, length)

# Extract the values from the array
cross_profile_values = [array[y, x] for y, x in cross_profile_indices]

# Output the values along the cross profile
print(cross_profile_values)

# Optional: Visualize the results
plt.imshow(array, cmap='gray')
y_coords, x_coords = zip(*cross_profile_indices)
plt.scatter(x_coords, y_coords, color='red')
plt.show()
