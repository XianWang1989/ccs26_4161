
import numpy as np
import matplotlib.pyplot as plt

def extract_diagonal_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    x_center, y_center = center
    radians = np.radians(angle)

    # Calculate the direction of the diagonal
    dx = np.cos(radians)
    dy = np.sin(radians)

    # Calculate the coordinates of the profile points
    profile = []
    for i in range(-length // 2, length // 2 + 1):
        x = int(x_center + i * dx)
        y = int(y_center + i * dy)

        # Check bounds
        if 0 <= x < cols and 0 <= y < rows:
            profile.append(array[y, x])

    return profile

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

# Extract the cross profile
cross_profile = extract_diagonal_cross_profile(array, center, angle, length)

# Print and visualize the cross profile
print("Cross Profile:", cross_profile)

# Optional: Plot the array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter([center[0] + i * np.cos(np.radians(angle)) for i in range(-length // 2, length // 2 + 1)],
            [center[1] + i * np.sin(np.radians(angle)) for i in range(-length // 2, length // 2 + 1)],
            color='red')
plt.title('Diagonally Extracted Cross Profile')
plt.show()
