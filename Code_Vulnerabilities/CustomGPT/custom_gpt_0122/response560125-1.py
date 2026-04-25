
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle, length):
    rows, cols = array.shape
    x_center, y_center = center
    angle_rad = np.radians(angle)

    # Calculate direction vectors for both diagonals
    dx = np.cos(angle_rad)
    dy = np.sin(angle_rad)

    # Create offsets for the cross profile
    offsets = np.arange(-length // 2, length // 2 + 1)

    # Calculate diagonal coordinates
    x1 = x_center + offsets * dx
    y1 = y_center + offsets * dy

    x2 = x_center + offsets * -dy
    y2 = y_center + offsets * dx

    # Clip coordinates to stay within the array bounds
    x1 = np.clip(x1, 0, cols - 1).astype(int)
    y1 = np.clip(y1, 0, rows - 1).astype(int)

    x2 = np.clip(x2, 0, cols - 1).astype(int)
    y2 = np.clip(y2, 0, rows - 1).astype(int)

    # Extract values from the array
    profile_1 = array[y1, x1]
    profile_2 = array[y2, x2]

    return profile_1, profile_2

# Example usage
array = np.random.rand(100, 100)  # Example 100x100 array
center = (50, 50)
angle = 25
length = 20

profile_1, profile_2 = extract_cross_profile(array, center, angle, length)

# Plot the results
plt.plot(profile_1, label='Diagonal 1 (25 degrees)')
plt.plot(profile_2, label='Diagonal 2 (25 degrees)')
plt.title('Cross Profile Extracted from 2D Array')
plt.legend()
plt.show()
