
import numpy as np

def extract_cross_profile(arr, center, angle, length):
    # Convert angle to radians
    theta = np.radians(angle)

    # Center point
    x_c, y_c = center

    # Calculate direction vectors
    dx = np.cos(theta)
    dy = np.sin(theta)

    # Generate indices for the cross profile
    indices = []
    for i in range(-length, length + 1):
        # Calculate coordinates for both diagonals
        x1 = int(x_c + i * dx)
        y1 = int(y_c + i * dy)
        x2 = int(x_c + i * dy)
        y2 = int(y_c - i * dx)

        # Append the valid indices
        if 0 <= x1 < arr.shape[0] and 0 <= y1 < arr.shape[1]:
            indices.append((x1, y1))
        if 0 <= x2 < arr.shape[0] and 0 <= y2 < arr.shape[1]:
            indices.append((x2, y2))

    # Extract values from the array
    values = [arr[x, y] for x, y in indices]

    return values

# Example usage
arr = np.random.rand(100, 100)  # Creating a random 100x100 array
center = (50, 50)
angle = 25
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)
print(cross_profile)
