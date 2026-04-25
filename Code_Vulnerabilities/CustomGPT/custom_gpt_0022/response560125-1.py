
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length=20):
    rows, cols = arr.shape
    x0, y0 = center
    angle_rad = np.radians(angle)

    # Calculate the offsets for the cross profile
    offsets = np.arange(-length, length + 1)
    x_diag = x0 + offsets * np.cos(angle_rad)
    y_diag = y0 + offsets * np.sin(angle_rad)

    # Clip the coordinates to ensure they are within array bounds
    x_diag = np.clip(x_diag, 0, cols - 1).astype(int)
    y_diag = np.clip(y_diag, 0, rows - 1).astype(int)

    # Extract the pixels along the diagonal cross
    profile = arr[y_diag, x_diag]

    return profile

# Create a sample 100x100 array
data = np.random.random((100, 100))

# Extract the cross profile
cross_profile = extract_cross_profile(data, center=(50, 50), angle=25)

# Display the original array and the cross profile
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("2D Array")
plt.imshow(data, cmap='viridis')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title("Cross Profile at 25 Degrees")
plt.plot(cross_profile)
plt.xlabel("Offset")
plt.ylabel("Value")
plt.grid()

plt.show()
