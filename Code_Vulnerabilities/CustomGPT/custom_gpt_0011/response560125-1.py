
import numpy as np

def extract_diagonal_cross_profile(array, center, angle, profile_length):
    # Convert angle to radians
    angle_rad = np.radians(angle)

    # Generate offsets based on the specified angle
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Prepare lists to hold the cross-profile coordinates
    coordinates = []

    # Generate the coordinates for the cross profile
    for i in range(-profile_length // 2, profile_length // 2 + 1):
        # Calculate coordinates for both diagonals
        x1 = int(center[0] + i * dx)  # Main diagonal
        y1 = int(center[1] + i * dy)
        x2 = int(center[0] + i * dy)  # Antidiagonal
        y2 = int(center[1] - i * dx)

        # Add coordinates if they are within the bounds of the array
        if 0 <= x1 < array.shape[0] and 0 <= y1 < array.shape[1]:
            coordinates.append(array[x1, y1])
        if 0 <= x2 < array.shape[0] and 0 <= y2 < array.shape[1]:
            coordinates.append(array[x2, y2])

    return np.array(coordinates)

# Example usage
array = np.random.random((100, 100))  # Create a 100x100 random array
center = (50, 50)                     # Center at (50, 50)
angle = 25                            # Angle of 25 degrees
profile_length = 21                   # Length of the cross profile

cross_profile = extract_diagonal_cross_profile(array, center, angle, profile_length)
print(cross_profile)
