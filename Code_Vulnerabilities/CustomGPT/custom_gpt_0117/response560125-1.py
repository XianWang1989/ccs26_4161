
import numpy as np

def extract_cross_profile(array, center, angle, length):
    # Convert angle to radians
    theta = np.radians(angle)

    # Calculate the direction vectors for the diagonal
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Determine the number of points in each direction
    x, y = center
    offsets = np.arange(-length // 2, length // 2 + 1)

    # Calculate the indices for the cross profile
    indices1 = [(int(x + offset * dx), int(y + offset * dy)) for offset in offsets]
    indices2 = [(int(x - offset * dx), int(y - offset * dy)) for offset in offsets]

    # Extract values from the array
    cross_values = []
    for i in indices1 + indices2:
        if 0 <= i[0] < array.shape[0] and 0 <= i[1] < array.shape[1]:
            cross_values.append(array[i])

    return np.array(cross_values)

# Example usage
arr = np.random.rand(100, 100)  # Create a 100x100 random array
center_point = (50, 50)         # Center at (50, 50)
angle = 25                       # Angle in degrees
length = 20                      # Length of the cross profile

cross_profile = extract_cross_profile(arr, center_point, angle, length)
print(cross_profile)
