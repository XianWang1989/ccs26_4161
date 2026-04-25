import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate

def extract_diagonal_cross_profile(arr, center, angle, width=1):
    """
    Extracts the cross profile of a 2D array at the given angle centered at the specified point.
    
    :param arr: 2D Numpy array
    :param center: tuple (x, y) - center of the cross profile
    :param angle: the angle of the diagonal cross in degrees
    :param width: width of the cross lines
    :return: the extracted cross profile
    """
    # Get the coordinates of the center
    x0, y0 = center

    # Create the coordinates of the array
    rows, cols = arr.shape
    x = np.arange(cols)
    y = np.arange(rows)

    # Create the mesh grid for the whole image
    X, Y = np.meshgrid(x, y)

    # Rotate the coordinates by the given angle to get the rotated cross
    angle_rad = np.deg2rad(angle)
    X_rot = np.cos(angle_rad) * (X - x0) - np.sin(angle_rad) * (Y - y0) + x0
    Y_rot = np.sin(angle_rad) * (X - x0) + np.cos(angle_rad) * (Y - y0) + y0

    # Extract values along the rotated diagonal line
    profile = []
    for i in range(rows):
        for j in range(cols):
            if abs(X_rot[i, j] - X_rot[x0, y0]) < width and abs(Y_rot[i, j] - Y_rot[x0, y0]) < width:
                profile.append(arr[i, j])

    return np.array(profile)

# Example usage
arr = np.random.rand(100, 100)  # 100x100 random array
center = (50, 50)  # center of the cross at (50, 50)
angle = 25  # angle of rotation for the diagonal

profile = extract_diagonal_cross_profile(arr, center, angle)

# Plotting the extracted profile
plt.plot(profile)
plt.title('Diagonal Cross Profile')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
