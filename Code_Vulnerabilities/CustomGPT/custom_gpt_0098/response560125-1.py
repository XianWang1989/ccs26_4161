
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length=20):
    cx, cy = center
    angle_rad = np.radians(angle)

    # Calculate offsets based on the angle
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Create line points
    x1, y1 = int(cx - dx), int(cy - dy)
    x2, y2 = int(cx + dx), int(cy + dy)

    # Extract the cross profile
    x_cross = np.linspace(x1, x2, 100).astype(int)
    y_cross = np.linspace(y1, y2, 100).astype(int)

    # Ensure coordinates are within the array bounds
    x_cross = np.clip(x_cross, 0, arr.shape[0] - 1)
    y_cross = np.clip(y_cross, 0, arr.shape[1] - 1)

    # Return the values along the cross profile
    return arr[y_cross, x_cross]

# Example usage
array = np.random.rand(100, 100)
cross_profile = extract_cross_profile(array, (50, 50), 25)

# Plotting
plt.plot(cross_profile)
plt.title("Cross Profile at 25 Degrees")
plt.xlabel("Profile Index")
plt.ylabel("Value")
plt.grid()
plt.show()
