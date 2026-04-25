
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 2D NumPy array
array = np.random.rand(100, 100)

# Function to extract the cross profile
def extract_cross_profile(arr, center, angle, length):
    cx, cy = center
    theta = np.radians(angle)  # Convert angle to radians

    # Calculate offsets for the diagonal cross
    x_offset = length * np.cos(theta)
    y_offset = length * np.sin(theta)

    # Generate the positions for the cross
    positions = []
    for sign in [-1, 1]:
        for dx, dy in [(x_offset, y_offset), (y_offset, x_offset)]:
            x = int(cx + sign * dx)
            y = int(cy + sign * dy)
            positions.append((x, y))

    # Extract values from the array at the calculated positions
    cross_profile = []
    for (x, y) in positions:
        if 0 <= x < arr.shape[0] and 0 <= y < arr.shape[1]:
            cross_profile.append(arr[x, y])

    return np.array(cross_profile)

# Center and angle for extraction
center = (50, 50)
angle = 25
length = 10  # Length of the cross arm

cross_profile = extract_cross_profile(array, center, angle, length)

print("Extracted cross profile:", cross_profile)

# Optional: Visualize the original array and the profile
plt.imshow(array, cmap='gray')
plt.scatter(*center, color='red')  # Center point
plt.title("Original Array with Center Point")
plt.show()
