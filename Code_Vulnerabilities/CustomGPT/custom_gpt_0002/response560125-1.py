
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(arr, center, angle, length):
    x_center, y_center = center
    angle_rad = np.deg2rad(angle)
    dx = length * np.cos(angle_rad)
    dy = length * np.sin(angle_rad)

    # Calculate diagonal indices
    indices = []
    for i in range(-length//2, length//2 + 1):
        x1 = int(x_center + i * dx)
        y1 = int(y_center + i * dy)
        x2 = int(x_center - i * dx)
        y2 = int(y_center - i * dy)
        if 0 <= x1 < arr.shape[1] and 0 <= y1 < arr.shape[0]:
            indices.append(arr[y1, x1])
        if 0 <= x2 < arr.shape[1] and 0 <= y2 < arr.shape[0]:
            indices.append(arr[y2, x2])

    return np.array(indices)

# Example usage
array_size = 100
arr = np.random.rand(array_size, array_size)
center = (50, 50)
angle = 25
length = 50  # Length of the cross profile

cross_profile = extract_cross_profile(arr, center, angle, length)

# Visualizing the original array and the cross profile
plt.imshow(arr, cmap='gray')
plt.title("2D Array")
plt.scatter([center[0]], [center[1]], color='red')  # Center point
plt.show()

print("Cross Profile:", cross_profile)
