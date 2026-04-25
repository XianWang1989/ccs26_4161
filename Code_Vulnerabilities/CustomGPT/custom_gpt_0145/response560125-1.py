
import numpy as np

def extract_cross_profile(arr, center, angle, length):
    """
    Extract a diagonal cross profile from a 2D array.

    Parameters:
    arr (np.ndarray): Input 2D numpy array.
    center (tuple): The (x, y) center point for extraction.
    angle (float): The angle in degrees.
    length (int): The length of the cross profile.

    Returns:
    np.ndarray: The diagonal cross profile as a 1D array.
    """
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate offsets
    dx = np.linspace(-length//2, length//2, length)
    dy = np.tan(angle_rad) * dx

    # Calculate diagonal coordinates
    x_coords = x_center + dx.astype(int)
    y_coords = y_center + dy.astype(int)

    # Clip to stay within the bounds of the array
    valid_mask = (x_coords >= 0) & (x_coords < arr.shape[1]) & (y_coords >= 0) & (y_coords < arr.shape[0])
    return arr[y_coords[valid_mask], x_coords[valid_mask]]

# Example usage
arr = np.random.rand(100, 100)  # Creating a 100x100 random array
center = (50, 50)
angle = 25
length = 20

cross_profile = extract_cross_profile(arr, center, angle, length)
print(cross_profile)
