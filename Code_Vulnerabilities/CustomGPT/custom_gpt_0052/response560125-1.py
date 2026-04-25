
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Generate points along the cross
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for d in range(-length, length + 1):
        # Calculate both diagonals
        x1.append(int(x_center + d * np.cos(angle_rad)))
        y1.append(int(y_center + d * np.sin(angle_rad)))
        x2.append(int(x_center + d * np.cos(angle_rad + np.pi/2)))
        y2.append(int(y_center + d * np.sin(angle_rad + np.pi/2)))

    # Filter points to stay within array boundaries
    points1 = [(x, y) for x, y in zip(x1, y1) if 0 <= x < cols and 0 <= y < rows]
    points2 = [(x, y) for x, y in zip(x2, y2) if 0 <= x < cols and 0 <= y < rows]

    # Extract values from the array
    profile_values = [array[y, x] for x, y in points1 + points2]

    return profile_values, points1 + points2

# Example usage
array = np.random.rand(100, 100)  # Replace with your 100x100 array
center = (50, 50)
angle = 25  # in degrees
length = 40  # half-length of the cross arm

profile, points = extract_cross_profile(array, center, angle, length)

# Display results
print("Extracted Cross Profile Values:", profile)
print("Points:", points)

# Optionally, visualize the array and cross profile
plt.imshow(array, cmap='gray')
for x, y in points:
    plt.plot(x, y, 'ro', markersize=2)
plt.show()
