
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    # Prepare to extract the cross profile
    cross_profile = []

    # Convert angle from degrees to radians
    theta = np.radians(angle)

    # Calculate the direction vectors
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Get the center coordinates
    x0, y0 = center

    # Calculate points along the diagonal lines
    for offset in range(-length // 2, length // 2 + 1):
        x1 = int(x0 + offset * dx)
        y1 = int(y0 + offset * dy)
        x2 = int(x0 + offset * dy)  # Swap dx, dy for the perpendicular line
        y2 = int(y0 - offset * dx)  # Swap dx, dy for the perpendicular line

        # Append values if within bounds
        if 0 <= x1 < array.shape[1] and 0 <= y1 < array.shape[0]:
            cross_profile.append(array[y1, x1])
        if 0 <= x2 < array.shape[1] and 0 <= y2 < array.shape[0]:
            cross_profile.append(array[y2, x2])

    return np.array(cross_profile)

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)                  # Center point
angle = 25                         # Angle in degrees
length = 20                        # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Display the results
print("Cross Profile Values:", cross_profile)

# Optional: visualize the original array
plt.imshow(array, cmap='gray')
plt.scatter([center[0]], [center[1]], color='red')  # Center point
plt.title('Original Array with Center Point')
plt.show()
