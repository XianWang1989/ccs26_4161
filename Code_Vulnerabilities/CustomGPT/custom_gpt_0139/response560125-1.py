
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    """
    Extracts a cross profile from a 2D numpy array at a specified angle.

    Parameters:
    - arr: 2D numpy array
    - center: Tuple (row, col) for the center of the cross
    - angle: Angle in degrees
    - length: Length of the cross arms

    Returns:
    - values along the cross profile
    """
    rows, cols = arr.shape
    row, col = center
    angle_rad = np.radians(angle)

    # Coordinates for the diagonal line
    diag_points = []
    for d in range(-length, length + 1):
        r_diag = row + d * np.sin(angle_rad)
        c_diag = col + d * np.cos(angle_rad)
        if 0 <= r_diag < rows and 0 <= c_diag < cols:
            diag_points.append(arr[int(round(r_diag)), int(round(c_diag))])

    # Coordinates for the anti-diagonal line (perpendicular)
    anti_diag_points = []
    for d in range(-length, length + 1):
        r_anti_diag = row + d * np.sin(angle_rad + np.pi / 2)
        c_anti_diag = col + d * np.cos(angle_rad + np.pi / 2)
        if 0 <= r_anti_diag < rows and 0 <= c_anti_diag < cols:
            anti_diag_points.append(arr[int(round(r_anti_diag)), int(round(c_anti_diag))])

    return diag_points + anti_diag_points

# Example usage
if __name__ == "__main__":
    # Create a 100x100 array with random numbers
    array_2d = np.random.rand(100, 100)

    # Extract the cross profile from the centered point (50, 50) at a 25-degree angle
    center_point = (50, 50)
    angle = 25  # degrees
    length = 20  # length of each arm of the cross

    cross_profile = extract_cross_profile(array_2d, center_point, angle, length)
    print("Cross Profile Values:", cross_profile)

    # Optionally visualize the original array and the cross profile
    plt.imshow(array_2d, cmap='gray')
    plt.scatter(center_point[1], center_point[0], color='red')  # center point
    plt.title('2D Array and Center Point')
    plt.show()
