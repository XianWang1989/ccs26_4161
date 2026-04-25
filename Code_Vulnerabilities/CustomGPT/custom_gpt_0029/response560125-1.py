
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    """
    Extracts a diagonal cross profile from a 2D array.

    Parameters:
    - array: 2D NumPy array.
    - center: Tuple (x, y) for the center point.
    - angle: Angle in degrees.
    - length: Length of the cross profile.

    Returns:
    - A list of values along the cross profile.
    """
    x, y = center
    angle_rad = np.radians(angle)

    # Calculate the offsets for the cross profile
    offsets = np.linspace(-length // 2, length // 2, length)

    # Calculate coordinate positions
    x_coords = x + offsets * np.cos(angle_rad)
    y_coords = y + offsets * np.sin(angle_rad)

    # Clip coordinates to stay within the bounds of the array
    x_coords = np.clip(x_coords, 0, array.shape[1] - 1).astype(int)
    y_coords = np.clip(y_coords, 0, array.shape[0] - 1).astype(int)

    # Extract values from the array
    cross_profile = array[y_coords, x_coords]

    return cross_profile

# Example usage
array = np.random.rand(100, 100)  # Create a 100x100 random array
center = (50, 50)  # Center point
angle = 25  # Angle in degrees
length = 50  # Length of the cross profile

cross_profile = extract_cross_profile(array, center, angle, length)

# Visualize the cross profile
plt.plot(cross_profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Profile Index')
plt.ylabel('Value')
plt.show()
