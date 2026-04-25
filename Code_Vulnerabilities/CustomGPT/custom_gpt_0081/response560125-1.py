
import numpy as np
import matplotlib.pyplot as plt

def extract_diagonal_cross(array, center, angle_degrees, length=20):
    # Convert angle from degrees to radians
    angle_radians = np.radians(angle_degrees)

    # Get center coordinates
    cx, cy = center

    # Calculate the slope of the diagonal lines
    slope = np.tan(angle_radians)

    # Prepare the coordinates for the cross profile
    cross_points = []
    for d in range(-length, length + 1):
        # Calculate the coordinates for both diagonal lines
        x1 = cx + d
        y1 = cy + int(slope * d)
        x2 = cx + d
        y2 = cy - int(slope * d)

        # Ensure coordinates are within the bounds of the array
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            cross_points.append(array[x1, y1])

        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            cross_points.append(array[x2, y2])

    return np.array(cross_points)

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Extract the cross profile centered at (50, 50) with an angle of 25 degrees
cross_profile = extract_diagonal_cross(array, center=(50, 50), angle_degrees=25)

# Output the cross profile
print("Diagonal Cross Profile:", cross_profile)

# Optional: Visualize the array and the cross profile
plt.imshow(array, cmap='gray')
plt.title('2D Numpy Array')
plt.scatter([50]*len(cross_profile), cross_profile, color='red')
plt.show()
