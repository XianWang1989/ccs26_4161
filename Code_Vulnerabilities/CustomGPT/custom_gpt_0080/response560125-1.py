
import numpy as np
import matplotlib.pyplot as plt

def get_cross_profile(arr, center, angle, length=20):
    rows, cols = arr.shape
    cx, cy = center
    angle_rad = np.radians(angle)

    # Create the offsets for the cross profile
    offsets = np.arange(-length, length + 1)

    # Calculate points for the diagonal
    x1 = np.array(cx + offsets * np.cos(angle_rad) - offsets * np.sin(angle_rad), dtype=int)
    y1 = np.array(cy + offsets * np.sin(angle_rad) + offsets * np.cos(angle_rad), dtype=int)

    # Calculate points for the anti-diagonal
    x2 = np.array(cx + offsets * np.cos(angle_rad) + offsets * np.sin(angle_rad), dtype=int)
    y2 = np.array(cy + offsets * np.sin(angle_rad) - offsets * np.cos(angle_rad), dtype=int)

    # Combine both segments
    x = np.concatenate((x1, x2))
    y = np.concatenate((y1, y2))

    # Filter out points that are out of bounds
    valid = (x >= 0) & (x < cols) & (y >= 0) & (y < rows)

    return x[valid], y[valid], arr[y[valid], x[valid]]

# Create a sample 100x100 array
array = np.random.rand(100, 100)

# Get the cross profile at (50, 50) with an angle of 25 degrees
x, y, profile = get_cross_profile(array, (50, 50), 25)

# Plot the results
plt.imshow(array, cmap='gray')
plt.scatter(x, y, color='red')
plt.title('Cross Profile at 25 Degrees')
plt.show()
