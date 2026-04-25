
import numpy as np
import matplotlib.pyplot as plt

def extract_diagonal_cross(array, center, angle, length):
    # Calculate the center and angle in radians
    cx, cy = center
    theta = np.radians(angle)

    # Calculate the direction vectors for the cross
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Prepare coordinates for both diagonal lines
    coords1 = []
    coords2 = []

    # Generate points along the cross
    for i in range(-length, length + 1):
        # Coordinates for the first diagonal
        x1 = int(cx + i * dy)
        y1 = int(cy + i * dx)

        # Coordinates for the second diagonal
        x2 = int(cx - i * dy)
        y2 = int(cy - i * dx)

        # Add coordinates if they are within the bounds of the array
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            coords1.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            coords2.append(array[x2, y2])

    # Combine the results
    return np.array(coords1 + coords2)

# Create a sample 100x100 2D NumPy array
array = np.random.rand(100, 100)

# Define the center and angle
center = (50, 50)
angle = 25  # in degrees
length = 50  # Length of the cross arms

# Extract the cross profile
cross_profile = extract_diagonal_cross(array, center, angle, length)

# Print the cross profile
print(cross_profile)

# Optional: Example visualization of the array and cross profile
plt.imshow(array, cmap='gray')
plt.scatter(center[1], center[0], color='red', label='Center (50,50)')
plt.title('2D NumPy Array with Cross Profile Center')
plt.legend()
plt.show()
