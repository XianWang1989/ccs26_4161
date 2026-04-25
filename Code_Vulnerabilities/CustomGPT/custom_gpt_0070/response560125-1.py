
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length=10):
    rows, cols = array.shape
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate the offsets based on length and angle
    offsets = np.arange(-length, length + 1)

    # Calculate coordinates for the diagonal lines
    diagonal_coords = [
        (int(x_center + offset * np.cos(angle_rad)), int(y_center + offset * np.sin(angle_rad)))
        for offset in offsets
    ]

    # Filter coordinates to stay within the array bounds
    valid_coords = [(x, y) for x, y in diagonal_coords if 0 <= x < rows and 0 <= y < cols]

    # Extract the values from the original array
    profile_values = [array[x, y] for x, y in valid_coords]

    return profile_values

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees

# Extract the cross profile
cross_profile = extract_cross_profile(array, center, angle)

# Print the resulting cross profile
print("Cross Profile Values:", cross_profile)

# Optional: visualize the original array and the cross profile
plt.imshow(array, cmap='gray')
plt.scatter(*center, color='red')  # Mark the center
plt.title('Original Array with Center Marked')
plt.show()
