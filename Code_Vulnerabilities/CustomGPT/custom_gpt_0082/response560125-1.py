
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 array
array = np.random.rand(100, 100)

# Function to extract the cross profile
def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    y, x = center
    angle_rad = np.deg2rad(angle)

    # Calculate the line endpoints
    dy = np.sin(angle_rad) * length
    dx = np.cos(angle_rad) * length

    # Create lists to hold the cross profile points
    points = []

    for d in range(-length, length + 1):
        # Calculate coordinates along the line
        new_x1 = int(x + dx * d)
        new_y1 = int(y + dy * d)
        new_x2 = int(x - dx * d)
        new_y2 = int(y - dy * d)

        # Check bounds and append points to profile
        if 0 <= new_x1 < cols and 0 <= new_y1 < rows:
            points.append(array[new_y1, new_x1])
        if 0 <= new_x2 < cols and 0 <= new_y2 < rows:
            points.append(array[new_y2, new_x2])

    return np.array(points)

# Extract cross profile
center = (50, 50)
angle = 25
length = 25  # Length of the cross profile
cross_profile = extract_cross_profile(array, center, angle, length)

# Plot the results
plt.plot(cross_profile)
plt.title("Cross Profile at 25 Degrees")
plt.xlabel("Distance Along Cross Profile")
plt.ylabel("Value")
plt.grid()
plt.show()
