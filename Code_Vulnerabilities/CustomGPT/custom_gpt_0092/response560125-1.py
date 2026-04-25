
import numpy as np

def extract_cross_profile(array, center, angle_degrees, length):
    angle_radians = np.radians(angle_degrees)
    x_center, y_center = center

    # Calculate the deltas for the diagonal
    delta_x = np.cos(angle_radians)
    delta_y = np.sin(angle_radians)

    # Generate coordinates along the diagonal
    x_coords = np.arange(-length // 2, length // 2 + 1)
    y_coords = np.round(y_center + (delta_y / delta_x) * (x_coords)).astype(int)

    # Calculate absolute x coordinates
    x_coords = np.round(x_center + x_coords).astype(int)

    # Filter coordinates to stay within array bounds
    valid_indices = (x_coords >= 0) & (x_coords < array.shape[1]) & (y_coords >= 0) & (y_coords < array.shape[0])
    x_coords = x_coords[valid_indices]
    y_coords = y_coords[valid_indices]

    # Extract the values from the array
    cross_profile_values = array[y_coords, x_coords]

    return cross_profile_values

# Example usage
array = np.random.rand(100, 100)  # Sample 100x100 array
center = (50, 50)
angle = 25
cross_profile = extract_cross_profile(array, center, angle, length=20)

print(cross_profile)
