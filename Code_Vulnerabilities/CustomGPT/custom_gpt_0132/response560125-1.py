
import numpy as np

def extract_cross_profile(array, center, angle, length):
    # Create the grid of coordinates
    x_center, y_center = center
    theta = np.radians(angle)

    # Calculate the offsets based on the angle
    x_offsets = np.linspace(-length//2, length//2, length)
    y_offsets = np.tan(theta) * x_offsets

    # Calculate the profile coordinates
    cross_x1 = np.array([x_center + x for x in x_offsets])
    cross_y1 = np.array([y_center + y for y in y_offsets])

    cross_x2 = np.array([x_center + x for x in x_offsets])
    cross_y2 = np.array([y_center - y for y in y_offsets])

    # Combine the coordinates
    cross_x = np.concatenate([cross_x1, cross_x2])
    cross_y = np.concatenate([cross_y1, cross_y2])

    # Clip coordinates to keep them within bounds
    cross_x = np.clip(cross_x, 0, array.shape[1] - 1)
    cross_y = np.clip(cross_y, 0, array.shape[0] - 1)

    # Extract the values from the array
    profile_values = array[cross_y.astype(int), cross_x.astype(int)]

    return profile_values

# Example usage
array = np.random.rand(100, 100)  # Create a random 100x100 array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 20  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)
print(cross_profile)
