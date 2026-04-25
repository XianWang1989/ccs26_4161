
import numpy as np

def extract_cross_profile(arr, center, angle_degrees, length):
    # Convert angle from degrees to radians
    angle_radians = np.radians(angle_degrees)
    # Calculate the direction vector
    dx = np.cos(angle_radians)
    dy = np.sin(angle_radians)

    # Extract coordinates for the profile
    coords = []
    for i in range(-length//2, length//2 + 1):
        x = int(center[0] + i * dx)
        y = int(center[1] + i * dy)
        # Only include coordinates within bounds
        if 0 <= x < arr.shape[0] and 0 <= y < arr.shape[1]:
            coords.append((x, y))

    # Extract the values from the array
    profile = [arr[x, y] for x, y in coords]
    return np.array(profile)

# Example usage
arr = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 21  # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)
print(cross_profile)
